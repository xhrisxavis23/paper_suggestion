# paper_suggestion — Claude Code orientation

> Two-layer research-topic discovery system: a Python collector keeps a 500-day rolling DB of academic paper metadata (≥ 2025-01-01 retained as of 2026-04), and a Claude Code skill runs a 4-bot pipeline (Trend → Gap → Skeptic → Proposer) over that DB to produce concrete research proposals.

## Layers

- **Layer 1: collector** (`collector/`) — Python CLI + cron. Daily scrape of arXiv / HuggingFace daily papers (default) plus OpenReview / Semantic Scholar (opt-in via `--with-or` / `--with-s2`), deduped into a monthly-partitioned JSONL DB at `metadb/`. No topic filtering at collect time — DB is "everything", filtering happens in Layer 2.
- **Layer 2: topic-finder skill** (`skills/topic_finder/`) — Claude Code skill (`/find-topic`). Expand keywords → match against rolling DB (substring or embedding) → cap+rank papers (default 200) → run 4 Sonnet calls with prompt-cached context (Trend-Analyzer, Gap-Hunter, Skeptic, Proposer) → emit Markdown report under `reports/`.

## Repo layout

```
collector/
  main.py                     # entry point: python -m collector.main
  backfill.py                 # python -m collector.backfill --start ... --end ...
  src/db.py                   # RollingDB (monthly-partitioned JSONL store + flock)
  src/scrapers/               # arxiv, huggingface, openreview, semantic_scholar
  src/{config,formatter,models}.py
skills/topic_finder/
  SKILL.md                    # /find-topic spec — read this for pipeline details
  prompts/*.md                # 4-bot prompts (expand, trend, gap, skeptic, proposer)
  scripts/{load_metadb,match_substring,match_embedding,build_report}.py
metadb/
  <YYMM>_rolling.jsonl        # 2602/2603/2604_rolling.jsonl etc. — DO NOT hand-edit
  daily/<YYYY-MM-DD>.md       # daily digest of newly-added papers (skipped on weekends)
  stats.json                  # latest run snapshot
  stats_history.jsonl         # append-only history (90-day retention via CI)
  .embeddings/                # FAISS index + ids (gitignored, only for --match-mode embedding)
  .lock                       # advisory file lock for concurrent writers
reports/<YYYY-MM-DD>-<slug>.md  # 4-bot output reports
docs/specs/                   # design doc
docs/plans/v0.2-backlog.md    # all v0.2 items shipped
docs/plans/v0.3-backlog.md    # v0.3 items (current version, all shipped)
docs/plans/v0.4-backlog.md    # v0.4 backlog (--deep PDF, journal coverage, Gemini bots)
tests/                        # pytest unit tests
.env.example                  # SEMANTIC_SCHOLAR_API_KEY, ANTHROPIC_API_KEY
.github/workflows/daily_collect.yml  # daily 06:00 UTC cron + pytest gate
```

## Commands

```bash
# venv (existing one is gitignored)
python -m venv .venv && source .venv/bin/activate
pip install -r collector/requirements.txt pytest

# Layer 1: collect (arxiv + hf default; --with-s2 / --with-or to opt in)
python -m collector.main                          # today, defaults
python -m collector.main --date 2026-04-26
python -m collector.main --with-s2                # include Semantic Scholar
python -m collector.main --with-or                # 12 venues pre-configured
python -m collector.backfill --start 2025-01-01 --end "$(date +%F)" --with-or

# Tests
pytest                                            # 40 unit tests, integration deselected
pytest -m integration                             # live network tests

# Layer 2: invoke from inside Claude Code
/find-topic "sparse autoencoder"
/find-topic "rag" --max-papers 150 --window 30
/find-topic "diffusion alignment" --match-mode embedding --top-k 200
```

## DB conventions (read before touching `metadb/`)

- **Monthly partitioning**: papers are stored in `<YYMM>_rolling.jsonl` (one file per calendar month based on `published_date`). `RollingDB.append` routes by month; `load_all` concatenates all `*_rolling.jsonl` files. Bumping individual files past ~30 MB means we should consider further partitioning.
- **Concurrent writers**: `RollingDB.append` and `prune` take an `fcntl.flock` on `metadb/.lock` — manual + cron overlap is safe.
- **No `id` field on disk**: the JSONL rows do *not* carry an `id` field. Readers compute it via `Paper.get_id()` at load time — this prevents stale ids from re-keying old rows if the formula changes.
- **`get_id()` formula**: `arxiv:<id-without-version>` if arxiv_id present, else `title:<lowercased+collapsed-whitespace>`.
- **`also_in` field**: when an HF paper shares an arxiv id with an existing arxiv row, the existing row's `also_in` list gains `"hf"` (the second-source curation signal isn't lost). The affected month file is rewritten in place.
- **`Paper.year`** is a `@property` derived from `published_date.year` — not a stored field.
- **Window**: `ROLLING_WINDOW_DAYS = 500` in `collector/src/config.py`. Prune drops papers whose `published_date < today − 500d` (cutoff ≈ 2024-12-14 as of 2026-04). Was 60d in v0.3 ship; bumped so 2025-01-01-and-later conference papers survive between cron runs. Rolling files containing only papers older than the cutoff are deleted entirely.
- **`metadb/daily/*.md`** holds *newly-added* papers only (post-dedup), not raw fetch lists. CI sweeps files older than 60 days. Weekend runs with no new papers skip the digest write entirely (arxiv has no Sat/Sun submissions).
- **`metadb/stats_history.jsonl`** is append-only (one row per collector run); CI prunes rows older than 90 days. Use it to trace when failures appeared.
- **`stats.json.failures`**: list[str] of partial failures (e.g. `"s2:AAAI:rate-limited (429)"`). Don't rely solely on `fetched_per_source` counts — soft failures don't show up there.

## Scraper gotchas

- **arXiv weekend rollback**: `_date_window` in `collector/src/scrapers/arxiv.py` extends the window backward through Sat/Sun, since arXiv has no weekend submissions. Monday runs pull Fri+Sat+Sun; Sat/Sun runs pull from preceding Friday.
- **arXiv 429 / timeout retry**: `_fetch_category` retries on `{429, 500, 502, 503, 504}` and `requests.Timeout` with exponential backoff (`ARXIV_RETRY_DELAYS = (5, 15, 45, 90)` seconds, 4 retries max). Final exhaustion propagates to `fetch()` and is recorded as a partial failure. Tuned for arXiv's IP throttle which can persist a few minutes after heavy backfill.
- **Semantic Scholar opt-in**: off by default in v0.3 because the public search-API rate-limits every venue to 0 without an API key. Use `--with-s2` and set `SEMANTIC_SCHOLAR_API_KEY` (in CI: `secrets.SEMANTIC_SCHOLAR_API_KEY`).
- **OpenReview opt-in**: off by default. Twelve venues now pre-configured in `OPENREVIEW_VENUE_IDS`: ICLR/ICML/NeurIPS use OR-native (`*.cc/<year>/Conference`) for in-progress submissions; AAAI / ACL / NAACL / EMNLP / IJCNLP (=AACL) / IJCAI / CVPR / ICCV / KDD use **dblp.org/conf/<UPPER>/<year>** because OR's `content.venueid` filter returns 0 for those venues' native ids — dblp imports backfill metadata after each conference finalizes. dblp imports use synthetic `cdate = Jan 1` of the conference year. Add new venues by appending to the list; the scraper already handles both forms (see `openreview.py:_fetch_venue` → `venue_short` extraction).
- **HuggingFace fallback loop**: if today's daily-papers list is empty, scraper walks back up to `HF_FALLBACK_DAYS` (default 3) and stops at the first non-empty day.
- **Concurrency**: `collector/main.py` runs all enabled scrapers in a `ThreadPoolExecutor` (one worker per source). Each scraper owns its own session, no shared state.
- **Backfill: OR/S2 are one-shot**: `collector/backfill.py` runs OR and S2 once before the per-day loop (their `fetch()` ignores `target_date` — OR returns the full venue snapshot, S2 uses its own rolling window). arXiv and HF still run per-day inside the loop. Pre-refactor (v0.3 ship) re-fetched OR every iteration — for a 482-day backfill that was ~5 hours wasted on duplicate API calls (DB dedup masked the bug).

## Skill / pipeline gotchas

- **Token budget (I-1)**: `match_substring(..., max_papers=N)` sorts by `(published_date DESC, venue_weight DESC)` and slices to N. Default cap is 200, which fits within Sonnet 200K context. Without the cap, popular topics ("rag", "agent") return 3K-6K matches → ~1M-2M token prompts that OOM. Always pass `--max-papers` from `/find-topic`.
- **Prompt caching (I-3)**: the matched-papers JSON block is identical across all 4 bots. SDK calls mark it as `cache_control={"type": "ephemeral"}` so it's cached after Trend-Analyzer's call → ~50% input-token savings on the 3 subsequent calls. Falls back to plain CLI calls if `ANTHROPIC_API_KEY` / `anthropic` SDK is missing.
- **`--window D`** on `/find-topic` maps to `--window-days D` on the match scripts.
- **`_short_id` format**: arxiv IDs render as `P-<arxiv-id>` (lossless); non-arxiv as `P-<VENUE>-<6hex>` (collision-resistant).
- **Author truncation**: ≤3 authors render verbatim; 4+ render as "first three, et al.".
- **`Paper.categories`** is currently arxiv-only. HF / OpenReview / S2 leave it `[]` — any future category-based filter must handle this.
- **Embedding mode** (`--match-mode embedding`) is opt-in heavyweight. Install `collector/requirements-embedding.txt` (sentence-transformers + faiss-cpu, ~2 GB with PyTorch). First run builds the index at `metadb/.embeddings/` (~30s for 30K papers).
- **4-bot pipeline orchestration** is documented in `skills/topic_finder/SKILL.md` (read it!). For non-interactive verification, `_run_pipeline.py` is a local driver (gitignored) that supports both SDK (cache_control) and CLI fallback.

## Style

- Match existing commit prefixes: `v0.X:`, `data:`, `demo:`, `docs:`, `chore:`.
- Korean prose is fine in user-facing reports / docstrings; internal code comments stay English.
- This project favors small dedicated modules over abstraction layers. Don't introduce frameworks; don't add dependencies beyond `requests` + `python-dateutil` for the collector.
- The `_run_pipeline.py` and `_backfill.sh` files at the repo root are personal verification drivers, gitignored. Don't promote them into the package.

## Where to look first

- Pipeline behaviour, CLI flags, scope-confirmation rules → `skills/topic_finder/SKILL.md`.
- Why a feature exists / what's deferred → `docs/specs/2026-04-26-paper-suggestion-design.md` and `docs/plans/v0.2-backlog.md`.
- Historical reasoning / commit context → `git log` (commit messages document the "why").
