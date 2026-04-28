---
name: find-topic
description: Analyze the rolling metadata DB (default 60-day window) for the user's keyword, then run a 4-bot pipeline (Trend-Analyzer → Gap-Hunter → Skeptic → Proposer) to produce a Markdown report containing trends, gaps, and concrete research proposals. Use when the user runs /find-topic or asks to find research gaps / proposals for a topic.
---

# topic-finder

Given a research topic keyword from the user, build `reports/YYYY-MM-DD-<slug>.md` containing:
1. trend clusters from the rolling metadata DB (default 60-day window),
2. validated research gaps,
3. concrete new research proposals,

all citing only papers present in the DB (no hallucinated references).

## Prerequisites

- `metadb/<YYMM>_rolling.jsonl` files exist (run `python -m collector.main` first if not).
- Python 3.11+ on PATH.
- Claude Sonnet 4.6 — this skill is intentionally Sonnet-tuned for cost.
- For embedding mode (`--match-mode embedding`): `pip install -r collector/requirements-embedding.txt`.
- For prompt-cached SDK mode: `pip install anthropic` and `ANTHROPIC_API_KEY` set. Without these, the pipeline still works via Claude Code CLI but skips explicit `cache_control`.

## Arguments

Parsed from `/find-topic "<keyword>" [options...]`:

| Arg | Default | Notes |
|-----|---------|-------|
| `<keyword>` | (required) | User's topic, free-form quoted string |
| `--top N` | 10 | Representative papers per cluster |
| `--clusters K` | 5 | Number of clusters Trend-Analyzer should output |
| `--proposals P` | 5 | Number of proposals Proposer should output |
| `--window D` | 60 | Rolling window days (must be ≤ DB window). Mapped to `--window-days D` on the match script. |
| `--max-papers M` | 200 | Hard cap on papers passed into the 4-bot pipeline (ranked by date desc + venue weight). Bounds Sonnet 200K context. |
| `--match-mode` | `substring` | `substring` (default) or `embedding` (sentence-transformers + FAISS, opt-in heavyweight) |
| `--expand-only` | off | Stop after keyword expansion + match (debug) |
| `--dry-run` | off | Show match count + token estimate then stop |
| `--output <path>` | `reports/YYYY-MM-DD-<slug>.md` | Output path |

## Pipeline

### §1. Keyword expansion

Read `prompts/expand_keywords.md` and replace `{TOPIC}` with the user keyword. Call Sonnet 4.6 once. Parse the JSON array. Save to `reports/.cache/<run-id>/expanded_keywords.json`.

### §2. Match against rolling DB

**Substring mode** (default):
```bash
python -m skills.topic_finder.scripts.match_substring \
    --rolling-dir metadb \
    --keywords-file reports/.cache/<run-id>/expanded_keywords.json \
    --out reports/.cache/<run-id>/matched.jsonl \
    --window-days <D> \
    --max-papers <M>
```

`--window-days` filters by `published_date ≥ today − D days`. `--max-papers` ranks the matched set by `(published_date DESC, venue_weight DESC)` and keeps the top M; venue weights live in `match_substring.py:_VENUE_WEIGHT` (top-tier venues outrank arXiv-only). The CLI prints `capped from <N>` when the cap activates.

**Embedding mode** (`--match-mode embedding`, opt-in):
```bash
python -m skills.topic_finder.scripts.match_embedding \
    --topic "<keyword>" --out reports/.cache/<run-id>/matched.jsonl \
    --window-days <D> --top-k <M>
```
First run builds a FAISS index at `metadb/.embeddings/` (~30s for 30K papers).

### §3. Scope confirmation (mandatory)

Show the user:

```
**Topic:** "<keyword>"
**Expanded keywords:** [...]
**매칭 논문:** <N>건 (rolling <D>d)  ← if N > <M>, "(capped from <N> to <M>)"
**클러스터 K = <K>, 제안 P = <P>, Sonnet 4.6**
**예상 토큰:** ~150K input, ~25K output
**예상 비용:** ~600원

Approve / 수정 / abort
```

If matched count < 10: warn and suggest a different / broader keyword.
If matched count > `--max-papers` (i.e., capping activated): explicitly tell the user how many were dropped and why (token budget) so they can narrow the keyword if they prefer different filtering.

If the user says abort, stop. If they suggest changes, re-run §1 with new keyword and repeat. Only proceed on explicit approval.

If `--dry-run`: print the summary and stop without §4–§7.
If `--expand-only`: stop after §3 print without §4–§7.

### §4–§7. 4-bot pipeline (Trend → Gap → Skeptic → Proposer)

Each bot reads its prompt from `prompts/`, fills in `{TOPIC}`, and is given the same `matched.jsonl` block (id, title, abstract truncated to 1500 chars, venue, date) as static input.

**Prompt caching (I-3)**: the matched-papers JSON block is identical across all four bots. Mark it as `cache_control={"type": "ephemeral"}` in the SDK call so it's cached after Trend-Analyzer's call and re-used by Gap-Hunter / Skeptic / Proposer. Empirically saves ~50% of input tokens billed (matched-papers is the bulk of input).

When using the SDK, structure each call as:
```python
client.messages.create(
    model="claude-sonnet-4-6",
    system=[
        {"type": "text", "text": <bot prompt>},
        {"type": "text", "text": <matched papers JSON>,
         "cache_control": {"type": "ephemeral"}},
    ],
    messages=[{"role": "user", "content": <bot-specific user block>}],
)
```

Save outputs to:
- `clusters.json` (Trend-Analyzer)
- `gaps.json` (Gap-Hunter)
- `gaps_validated.json` (Skeptic — `{passed: [...], rejected: [...]}`)
- `proposals.json` (Proposer)

### §8. Build report

```bash
python -m skills.topic_finder.scripts.build_report \
    --topic "<keyword>" \
    --expanded-file reports/.cache/<run-id>/expanded_keywords.json \
    --matched-file reports/.cache/<run-id>/matched.jsonl \
    --clusters-file reports/.cache/<run-id>/clusters.json \
    --gaps-validated-file reports/.cache/<run-id>/gaps_validated.json \
    --proposals-file reports/.cache/<run-id>/proposals.json \
    --window-days <D> \
    --output reports/<YYYY-MM-DD>-<slug>.md
```

### §9. Final report to user

Tell the user:
- the absolute path to the generated report,
- the cluster / gap / proposal counts,
- total tokens used (input + output, with cached input broken out separately when SDK is used),
- whether the result was capped at `--max-papers`.

## Display conventions

- **Author truncation**: papers with ≤3 authors render every author by name; papers with 4+ render the first 3 followed by ` et al.`.
- **Reference IDs**: `P-<arxiv-id>` for arxiv papers (lossless); `P-<VENUE>-<6-hex>` for non-arxiv papers (collision-resistant short hash of the full paper id).
- **Bibliography (Section 4)** is grouped by cluster — each paper appears under its cluster's heading; matched papers not in any cluster's `paper_ids` go to a "기타" group.
- **`also_in` annotations**: when a paper appears in multiple sources (e.g., arxiv + HF), the bibliography line includes `also_in: hf` so the second-source curation signal isn't lost.
- **DB window header**: `build_report` prints `(<N>d)` computed from the actual `(start, end)` range, not a fixed string.

## Failure handling

- If keyword expansion returns < 3 keywords or non-JSON: retry once with the same prompt; if still bad, fail with explicit message.
- If matched count is 0 even after retry with broader expansion: stop and ask user to broaden their topic.
- If a single bot returns malformed JSON: retry once with stricter "Return JSON only, no prose" preamble; if still malformed, save the raw output to the cache dir and fail with the path.
- If any LLM call hits rate limit: wait 60s and retry once.

## Out-of-scope (v0.3)

- PDF body analysis (`--deep` integration with paper_search) — still deferred.
- Personalization based on user's prior reads.
- Slack/Discord webhook notifications.
- Trend visualization (matplotlib SVG of cluster growth over time).
- Multi-evaluator personas in Skeptic.
- Auto-classifier for sub-domain.
