---
name: topic-finder
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

## Arguments

Parsed from `/find-topic "<keyword>" [options...]`:

| Arg | Default | Notes |
|-----|---------|-------|
| `<keyword>` | (required) | User's topic, free-form quoted string |
| `--top N` | 10 | Representative papers per cluster |
| `--clusters K` | 5 | Number of clusters Trend-Analyzer should output |
| `--proposals P` | 5 | Number of proposals Proposer should output |
| `--window D` | 60 | Rolling window days (must be ≤ DB window). Mapped to `--window-days D` on the match script. |
| `--expand-only` | off | Stop after keyword expansion + match (debug) |
| `--dry-run` | off | Show match count + token estimate then stop |
| `--output <path>` | `reports/YYYY-MM-DD-<slug>.md` | Output path |

## Pipeline

### §1. Keyword expansion

Read `prompts/expand_keywords.md` and replace `{TOPIC}` with the user keyword. Call Sonnet 4.6 once. Parse the JSON array. Save to `reports/.cache/<run-id>/expanded_keywords.json`.

### §2. Match against rolling DB

Run:
```bash
python -m skills.topic_finder.scripts.match_substring \
    --rolling-dir metadb \
    --keywords-file reports/.cache/<run-id>/expanded_keywords.json \
    --out reports/.cache/<run-id>/matched.jsonl \
    --window-days <D>
```

`--window-days` filters the rolling DB to papers with `published_date` ≥ `today - D days` before substring matching. Defaults to no filter (uses the full DB).

Read the match count.

### §3. Scope confirmation (mandatory)

Show the user:

```
**Topic:** "<keyword>"
**Expanded keywords:** [...]
**매칭 논문:** <N>건 (rolling <D>d)
**클러스터 K = <K>, 제안 P = <P>, Sonnet 4.6**
**예상 토큰:** ~150K input, ~25K output
**예상 비용:** ~600원

Approve / 수정 / abort
```

If matched count < 10: warn and suggest a different / broader keyword. If > 500: warn and suggest narrowing.

If the user says abort, stop. If they suggest changes, re-run §1 with new keyword and repeat. Only proceed on explicit approval.

If `--dry-run`: print the summary and stop without §4–§7.
If `--expand-only`: stop after §3 print without §4–§7.

### §4. Trend-Analyzer

Read `prompts/trend_analyzer.md`, fill in `{TOPIC}`, append matched papers (id, title, abstract, venue, date — keep abstract <= 1500 chars per paper to bound input). Single Sonnet 4.6 call. Parse the JSON array. Save to `reports/.cache/<run-id>/clusters.json`.

### §5. Gap-Hunter

Read `prompts/gap_hunter.md`, append clusters.json + matched papers. Single Sonnet call. Save to `gaps.json`.

### §6. Skeptic

Read `prompts/skeptic.md`, append gaps.json + clusters.json + matched papers. Single Sonnet call. Save to `gaps_validated.json`.

### §7. Proposer

Read `prompts/proposer.md`, append gaps_validated.passed + clusters + matched. Single Sonnet call. Save to `proposals.json`.

### §8. Build report

Run:
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
- total tokens used.

## Display conventions

- **Author truncation**: papers with ≤3 authors render every author by name; papers with 4+ render the first 3 followed by ` et al.`. So a paper with exactly 3 authors shows all three (no et al.).
- **Reference IDs**: `P-<arxiv-id>` for arxiv papers (lossless); `P-<VENUE>-<6-hex>` for non-arxiv papers (collision-resistant short hash of the full paper id).
- **DB window header**: `build_report` prints `(<N>d)` where N is computed from the actual `(start, end)` range, not a fixed string.

## Failure handling

- If keyword expansion returns < 3 keywords or non-JSON: retry once with the same prompt; if still bad, fail with explicit message.
- If matched count is 0 even after retry with broader expansion: stop and ask user to broaden their topic.
- If a single bot returns malformed JSON: retry once with stricter "Return JSON only, no prose" preamble; if still malformed, save the raw output to the cache dir and fail with the path.
- If any LLM call hits rate limit: wait 60s and retry once.

## Out-of-scope (v0.2)

- PDF body analysis (`--deep` integration with paper_search) — still deferred.
- Embedding-based matching — substring only.
- Personalization based on user's prior reads.
- Slack/Discord webhook notifications.
- Trend visualization (matplotlib SVG of cluster growth over time).
- Multi-evaluator personas in Skeptic.
