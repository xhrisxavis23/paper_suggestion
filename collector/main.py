"""Daily collector entry point.

Run:
    python -m collector.main                  # today's date
    python -m collector.main --date 2026-04-26
    python -m collector.main --skip-arxiv     # skip a slow source
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from datetime import date
from pathlib import Path

from .src.config import (
    DAILY_DIR,
    METADB_DIR,
    ROLLING_JSONL,
    ROLLING_WINDOW_DAYS,
    STATS_JSON,
)
from .src.db import RollingDB
from .src.formatter import format_daily_digest
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
    p = argparse.ArgumentParser(description="paper_suggestion daily collector")
    p.add_argument("--date", default=str(date.today()))
    p.add_argument("--skip-arxiv", action="store_true")
    p.add_argument("--skip-hf", action="store_true")
    p.add_argument("--skip-or", action="store_true")
    p.add_argument("--skip-s2", action="store_true")
    p.add_argument("--root", default=".",
                   help="Repo root (paths under metadb/ are resolved here)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        target_date = date.fromisoformat(args.date)
    except ValueError:
        logger.error("Invalid --date: %s", args.date)
        return 2

    root = Path(args.root)
    rolling_path = root / ROLLING_JSONL
    daily_dir = root / DAILY_DIR
    stats_path = root / STATS_JSON
    daily_dir.mkdir(parents=True, exist_ok=True)

    all_papers = []
    counts: dict[str, int] = {}

    if not args.skip_arxiv:
        try:
            ps = ArxivScraper().fetch(target_date)
            all_papers.extend(ps)
            counts["arxiv"] = len(ps)
        except Exception as e:
            logger.error("arXiv failed: %s", e)
            counts["arxiv"] = 0

    if not args.skip_hf:
        try:
            ps = HuggingFaceScraper().fetch(target_date)
            all_papers.extend(ps)
            counts["hf"] = len(ps)
        except Exception as e:
            logger.error("HF failed: %s", e)
            counts["hf"] = 0

    if not args.skip_or:
        try:
            ps = OpenReviewScraper().fetch(target_date)
            all_papers.extend(ps)
            counts["openreview"] = len(ps)
        except Exception as e:
            logger.error("OpenReview failed: %s", e)
            counts["openreview"] = 0

    if not args.skip_s2:
        try:
            ps = SemanticScholarScraper().fetch(target_date)
            all_papers.extend(ps)
            counts["s2"] = len(ps)
        except Exception as e:
            logger.error("S2 failed: %s", e)
            counts["s2"] = 0

    db = RollingDB(rolling_path)
    added = db.append(all_papers)
    pruned = db.prune(today=target_date, window_days=ROLLING_WINDOW_DAYS)

    digest_md = format_daily_digest(all_papers, target_date)
    daily_path = daily_dir / f"{target_date}.md"
    daily_path.write_text(digest_md, encoding="utf-8")

    total_in_db = len(db.load_all())
    stats = {
        "last_run": target_date.isoformat(),
        "fetched_per_source": counts,
        "total_fetched": len(all_papers),
        "added_to_db": added,
        "pruned": pruned,
        "total_in_rolling": total_in_db,
    }
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    stats_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")

    logger.info("Daily collect done: fetched=%d, added=%d, pruned=%d, in_db=%d",
                len(all_papers), added, pruned, total_in_db)
    return 0


if __name__ == "__main__":
    sys.exit(main())
