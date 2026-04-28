"""Daily collector entry point.

Run:
    python -m collector.main                    # today's date, arxiv + hf
    python -m collector.main --date 2026-04-26  # specific date
    python -m collector.main --skip-arxiv       # skip a default source
    python -m collector.main --with-s2          # opt in to Semantic Scholar
    python -m collector.main --with-or          # opt in to OpenReview

OpenReview and Semantic Scholar are off by default in v0.3 because in the
typical configuration both contribute zero rows to the rolling window
(OR submission cdates are pre-cutoff; S2 search-API rate-limits without
an API key). Opt in only when the surrounding env supports them.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone
from pathlib import Path
from typing import List, Tuple

from .src.config import (
    DAILY_DIR,
    METADB_DIR,
    ROLLING_DIR,
    ROLLING_WINDOW_DAYS,
    STATS_HISTORY_JSONL,
    STATS_JSON,
)
from .src.db import RollingDB
from .src.formatter import format_daily_digest
from .src.scrapers.arxiv import ArxivScraper
from .src.scrapers.huggingface import HuggingFaceScraper
from .src.scrapers.journal import JournalScraper
from .src.scrapers.openreview import OpenReviewScraper
from .src.scrapers.semantic_scholar import SemanticScholarScraper

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="paper_suggestion daily collector")
    p.add_argument("--date", default=str(date.today()))
    p.add_argument("--skip-arxiv", action="store_true",
                   help="Skip arXiv (on by default).")
    p.add_argument("--skip-hf", action="store_true",
                   help="Skip HuggingFace daily papers (on by default).")
    p.add_argument("--with-or", action="store_true",
                   help="Include OpenReview (off by default — most submissions "
                        "are dated pre-cutoff and get 100%% pruned).")
    p.add_argument("--with-s2", action="store_true",
                   help="Include Semantic Scholar (off by default — requires "
                        "SEMANTIC_SCHOLAR_API_KEY to return data).")
    p.add_argument("--with-journal", action="store_true",
                   help="Include OpenAlex journal pulls per JOURNAL_TARGETS "
                        "(off by default; one-shot per run, ignores --date).")
    p.add_argument("--root", default=".",
                   help="Repo root (paths under metadb/ are resolved here)")
    return p.parse_args()


def _run_source(name: str, scraper, target_date: date) -> Tuple[List, List[str], str | None]:
    """Run one scraper. Return (papers, scraper_failures, fatal_error)."""
    try:
        ps = scraper.fetch(target_date)
    except Exception as e:
        logger.error("%s failed: %s", name, e)
        return [], [], f"{name}:fatal:{type(e).__name__}: {e}"
    return ps, list(getattr(scraper, "failures", []) or []), None


def main() -> int:
    args = parse_args()
    try:
        target_date = date.fromisoformat(args.date)
    except ValueError:
        logger.error("Invalid --date: %s", args.date)
        return 2

    root = Path(args.root)
    rolling_dir = root / ROLLING_DIR
    daily_dir = root / DAILY_DIR
    stats_path = root / STATS_JSON
    history_path = root / STATS_HISTORY_JSONL
    daily_dir.mkdir(parents=True, exist_ok=True)

    plan: list[tuple[str, object]] = []
    if not args.skip_arxiv:
        plan.append(("arxiv", ArxivScraper()))
    if not args.skip_hf:
        plan.append(("hf", HuggingFaceScraper()))
    if args.with_or:
        plan.append(("openreview", OpenReviewScraper()))
    if args.with_s2:
        plan.append(("s2", SemanticScholarScraper()))
    if args.with_journal:
        plan.append(("journal", JournalScraper()))

    all_papers: list = []
    counts: dict[str, int] = {}
    failures: List[str] = []

    # Run scrapers in parallel — each uses its own session, no shared state.
    with ThreadPoolExecutor(max_workers=max(1, len(plan))) as ex:
        results = list(ex.map(
            lambda nc: (nc[0], *_run_source(nc[0], nc[1], target_date)),
            plan,
        ))
    for name, papers, src_failures, fatal in results:
        all_papers.extend(papers)
        counts[name] = len(papers)
        failures.extend(src_failures)
        if fatal:
            failures.append(fatal)

    db = RollingDB(rolling_dir)
    new_papers = db.append(all_papers)
    pruned = db.prune(today=target_date, window_days=ROLLING_WINDOW_DAYS)

    # M-1: arXiv has no Sat/Sun submissions; an empty digest on those days is
    # noise rather than signal. Skip writing on weekends if nothing new came in.
    daily_path = daily_dir / f"{target_date}.md"
    is_weekend = target_date.weekday() in (5, 6)
    if is_weekend and not new_papers:
        logger.info("Weekend with no new papers — skipping digest write (%s)",
                    daily_path)
    else:
        digest_md = format_daily_digest(new_papers, target_date)
        daily_path.write_text(digest_md, encoding="utf-8")

    total_in_db = len(db.load_all())
    stats = {
        "last_run": target_date.isoformat(),
        "ran_at": datetime.now(timezone.utc).isoformat(),
        "fetched_per_source": counts,
        "total_fetched": len(all_papers),
        "added_to_db": len(new_papers),
        "pruned": pruned,
        "total_in_rolling": total_in_db,
        "failures": failures,
    }
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    stats_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")

    # I-4: append-only history alongside the latest-snapshot stats.json.
    with history_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(stats, ensure_ascii=False) + "\n")

    logger.info("Daily collect done: fetched=%d, added=%d, pruned=%d, in_db=%d, failures=%d",
                len(all_papers), len(new_papers), pruned, total_in_db, len(failures))
    return 0


if __name__ == "__main__":
    sys.exit(main())
