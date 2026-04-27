# paper_suggestion — Claude Code orientation

> Two-layer research-topic discovery system: a Python collector keeps a 60-day rolling DB of academic paper metadata, and a Claude Code skill runs a 4-bot pipeline (Trend → Gap → Skeptic → Proposer) over that DB to produce concrete research proposals.

## Layers

- **Layer 1: collector** (`collector/`) — Python CLI + cron. Daily scrape of arXiv / HuggingFace daily papers / OpenReview / Semantic Scholar, deduped into a monthly-partitioned JSONL DB at `metadb/`. No topic filtering at collect time — DB is "everything", filtering happens in Layer 2.
- **Layer 2: topic-finder skill** (`skills/topic_finder/`) — Claude Code skill (`/find-topic`). Expand keywords → substring-match against rolling DB → run 4 Sonnet calls (Trend-Analyzer, Gap-Hunter, Skeptic, Proposer) → emit Markdown report under `reports/`.

## Repo layout

```
collector/
  main.py                     # entry point: python -m collector.main
  src/db.py                   # RollingDB (monthly-partitioned JSONL store)
  src/scrapers/               # arxiv, huggingface, openreview, semantic_scholar
  src/{config,formatter,models}.py
skills/topic_finder/
  SKILL.md                    # /find-topic spec — read this for pipeline details
  prompts/*.md                # 4-bot prompts (expand, trend, gap, skeptic, proposer)
  scripts/{load_metadb,match_substring,build_report}.py
metadb/
  <YYMM>_rolling.jsonl        # 2602/2603/2604_rolling.jsonl etc. — DO NOT hand-edit
  daily/<YYYY-MM-DD>.md       # human-readable daily digest of newly-added papers
  stats.json                  # last_run, per-source counts, failures
reports/<YYYY-MM-DD>-<slug>.md  # 4-bot output reports
docs/specs/                   # design doc
docs/plans/v0.2-backlog.md    # historical backlog (all items shipped in v0.2)
tests/                        # pytest unit tests
.github/workflows/daily_collect.yml  # daily 06:00 UTC cron
```

## Commands

```bash
# venv (existing one is gitignored)
python -m venv .venv && source .venv/bin/activate
pip install -r collector/requirements.txt pytest

# Layer 1: collect
python -m collector.main                          # today
python -m collector.main --date 2026-04-26
python -m collector.main --skip-or --skip-s2      # arxiv+HF only (faster)

# Tests
pytest                                            # 29 unit tests, integration deselected
pytest -m integration                             # live network tests

# Layer 2: invoke from inside Claude Code
/find-topic "sparse autoencoder"
/find-topic "diffusion alignment" --clusters 7 --proposals 3 --window 30
```

## DB conventions (read before touching `metadb/`)

- **Monthly partitioning**: papers are stored in `<YYMM>_rolling.jsonl` (one file per calendar month based on `published_date`). `RollingDB.append` routes by month; `load_all` concatenates all `*_rolling.jsonl` files. Bumping individual files past ~30 MB means we should consider further partitioning.
- **No `id` field on disk**: the JSONL rows do *not* carry an `id` field. Readers compute it via `Paper.get_id()` at load time — this prevents stale ids from re-keying old rows if the formula changes.
- **`get_id()` formula**: `arxiv:<id-without-version>` if arxiv_id present, else `title:<lowercased+collapsed-whitespace>`.
- **Window**: `ROLLING_WINDOW_DAYS = 60` in `collector/src/config.py`. Prune drops papers whose `published_date < today − 60d`. Rolling files containing only papers older than the cutoff are deleted entirely.
- **`metadb/daily/*.md`** holds *newly-added* papers only (post-dedup), not raw fetch lists. CI sweeps files older than 60 days.
- **`stats.json.failures`**: list[str] of partial failures (e.g. `"s2:AAAI:rate-limited (429)"`). Don't rely solely on `fetched_per_source` counts — soft failures don't show up there.

## Scraper gotchas

- **arXiv weekend rollback**: `_date_window` in `collector/src/scrapers/arxiv.py` extends the window backward through Sat/Sun, since arXiv has no weekend submissions. Monday runs pull Fri+Sat+Sun; Sat/Sun runs pull from preceding Friday.
- **Semantic Scholar without an API key**: the public search-API rate-limits each venue to 0 in practice. Set `SEMANTIC_SCHOLAR_API_KEY` (passed via `secrets.SEMANTIC_SCHOLAR_API_KEY` in CI) to get real venue data.
- **OpenReview**: only `ICLR.cc/2026/Conference` configured. Most submissions are dated 2025-09 (pre-cutoff) → 100 % pruned in the 60-day window. Wait for active venues with recent `cdate` before expecting OR coverage.
- **HuggingFace fallback loop**: if today's daily-papers list is empty, scraper walks back up to `HF_FALLBACK_DAYS` (default 3) and stops at the first non-empty day.

## Skill / pipeline gotchas

- **`--window D`** on `/find-topic` maps to `--window-days D` on `match_substring.py`. SKILL.md still uses the cosmetic `--window` form.
- **`_short_id` format**: arxiv IDs render as `P-<arxiv-id>` (lossless); non-arxiv as `P-<VENUE>-<6hex>` (collision-resistant).
- **Author truncation**: ≤3 authors render verbatim; 4+ render as "first three, et al.".
- **`Paper.categories`** is currently arxiv-only. HF / OpenReview / S2 leave it `[]` — any future category-based filter must handle this.
- **4-bot pipeline orchestration** is documented in `skills/topic_finder/SKILL.md` (read it!). For non-interactive verification, `_run_pipeline.py` is a local driver (gitignored) that mirrors the SKILL.md flow via the `claude` CLI.

## Style

- Match existing commit prefixes: `v0.X:`, `data:`, `demo:`, `docs:`, `chore:`.
- Korean prose is fine in user-facing reports / docstrings; internal code comments stay English.
- This project favors small dedicated modules over abstraction layers. Don't introduce frameworks; don't add dependencies beyond `requests` + `python-dateutil` for the collector.
- The `_run_pipeline.py` and `_backfill.sh` files at the repo root are personal verification drivers, gitignored. Don't promote them into the package.

## Where to look first

- Pipeline behaviour, CLI flags, scope-confirmation rules → `skills/topic_finder/SKILL.md`.
- Why a feature exists / what's deferred → `docs/specs/2026-04-26-paper-suggestion-design.md` and `docs/plans/v0.2-backlog.md`.
- Historical reasoning / commit context → `git log` (commit messages document the "why").
