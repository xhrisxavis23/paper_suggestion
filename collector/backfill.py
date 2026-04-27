"""Backfill the rolling DB by iterating over a date range.

Run:
    python -m collector.backfill --start 2026-02-26 --end 2026-04-27
    python -m collector.backfill --days 60                  # last N days back from today
    python -m collector.backfill --start 2026-04-01 --with-s2

Each day is a separate `python -m collector.main --date YYYY-MM-DD` invocation
under the hood, so all dedup / prune / failure-tracking semantics are identical.
At the end, prints final coverage by month so you can spot gaps quickly.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

from .src.config import ROLLING_DIR
from .src.db import RollingDB
from .main import _run_source, parse_args as _main_parse_args  # noqa: F401
from .src.scrapers.arxiv import ArxivScraper
from .src.scrapers.huggingface import HuggingFaceScraper
from .src.scrapers.openreview import OpenReviewScraper
from .src.scrapers.semantic_scholar import SemanticScholarScraper

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="paper_suggestion backfill")
    p.add_argument("--start", help="Inclusive start date YYYY-MM-DD.")
    p.add_argument("--end", help="Inclusive end date YYYY-MM-DD (default today).")
    p.add_argument("--days", type=int,
                   help="Alternative to --start: backfill the last N days "
                        "ending at --end (default today).")
    p.add_argument("--skip-arxiv", action="store_true")
    p.add_argument("--skip-hf", action="store_true")
    p.add_argument("--with-or", action="store_true")
    p.add_argument("--with-s2", action="store_true")
    p.add_argument("--root", default=".")
    return p.parse_args()


def _resolve_range(args: argparse.Namespace) -> tuple[date, date]:
    end = date.fromisoformat(args.end) if args.end else date.today()
    if args.start:
        start = date.fromisoformat(args.start)
    elif args.days:
        start = end - timedelta(days=args.days - 1)
    else:
        raise SystemExit("error: pass either --start or --days")
    if start > end:
        raise SystemExit(f"error: --start ({start}) is after --end ({end})")
    return start, end


def _build_plan(args: argparse.Namespace):
    plan = []
    if not args.skip_arxiv:
        plan.append(("arxiv", ArxivScraper()))
    if not args.skip_hf:
        plan.append(("hf", HuggingFaceScraper()))
    if args.with_or:
        plan.append(("openreview", OpenReviewScraper()))
    if args.with_s2:
        plan.append(("s2", SemanticScholarScraper()))
    return plan


def main() -> int:
    args = parse_args()
    start, end = _resolve_range(args)
    root = Path(args.root)
    rolling_dir = root / ROLLING_DIR
    db = RollingDB(rolling_dir)

    days = (end - start).days + 1
    logger.info("Backfilling %d day(s): %s → %s", days, start, end)

    total_added = 0
    total_failures: list[str] = []
    cur = start
    idx = 0
    while cur <= end:
        idx += 1
        plan = _build_plan(args)  # fresh scrapers per day so .failures resets cleanly
        all_papers = []
        for name, scraper in plan:
            ps, src_failures, fatal = _run_source(name, scraper, cur)
            all_papers.extend(ps)
            total_failures.extend(src_failures)
            if fatal:
                total_failures.append(fatal)
        new_papers = db.append(all_papers)
        total_added += len(new_papers)
        logger.info("[%d/%d] %s: fetched=%d added=%d", idx, days, cur,
                    len(all_papers), len(new_papers))
        cur += timedelta(days=1)

    # Final coverage report.
    all_loaded = db.load_all()
    by_month = Counter()
    for p in all_loaded:
        if p.published_date:
            by_month[p.published_date.strftime("%Y-%m")] += 1
    print("\n=== Backfill complete ===")
    print(f"Days processed:    {days}")
    print(f"Papers added:      {total_added}")
    print(f"Total in DB:       {len(all_loaded)}")
    print(f"Failures recorded: {len(total_failures)}")
    print("Coverage by month (in DB after backfill):")
    for ym in sorted(by_month):
        print(f"  {ym}: {by_month[ym]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
