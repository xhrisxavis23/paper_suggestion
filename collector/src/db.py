"""Rolling JSONL metadata database, partitioned by month.

On-disk layout:

    <root>/
        2602_rolling.jsonl
        2603_rolling.jsonl
        2604_rolling.jsonl
        ...

Each file holds papers whose `published_date` falls in that calendar month
(YY = last two digits of year, MM = month). Splitting keeps individual files
under GitHub's 50 MB recommendation and bounds rewrites on prune.
"""
from __future__ import annotations

import json
import logging
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable, List

from .models import Paper

logger = logging.getLogger(__name__)

ROLLING_GLOB = "*_rolling.jsonl"


def _month_key(d: date) -> str:
    return d.strftime("%y%m")


class RollingDB:
    """Append-only monthly-partitioned JSONL DB with id-based dedup +
    date-based prune.

    Note: `append` re-reads every month file on every call (O(n) per call,
    O(n*m) if called m times for chunked input). Fine at current scale; if
    backfill ever calls in tight loops, lift the existing-id set into a
    long-lived caller and skip re-reads.
    """

    def __init__(self, root: Path):
        self.root = Path(root)

    def _month_path(self, d: date) -> Path:
        return self.root / f"{_month_key(d)}_rolling.jsonl"

    def _all_files(self) -> List[Path]:
        if not self.root.exists():
            return []
        return sorted(self.root.glob(ROLLING_GLOB))

    def load_all(self) -> List[Paper]:
        out: List[Paper] = []
        for f in self._all_files():
            with f.open("r", encoding="utf-8") as fp:
                for line in fp:
                    line = line.strip()
                    if not line:
                        continue
                    out.append(Paper.from_jsonl_dict(json.loads(line)))
        return out

    def append(self, papers: Iterable[Paper]) -> List[Paper]:
        """Append unseen papers; return the list of newly-written papers
        in input order. Dedups against existing rows AND in-batch duplicates.
        Papers with no `published_date` are skipped (no monthly bucket)."""
        existing_ids = {p.get_id() for p in self.load_all()}
        seen_in_batch: set[str] = set()
        new_papers: List[Paper] = []
        per_month: dict[str, List[Paper]] = {}
        skipped_no_date = 0

        for p in papers:
            pid = p.get_id()
            if pid in existing_ids or pid in seen_in_batch:
                continue
            if p.published_date is None:
                skipped_no_date += 1
                continue
            seen_in_batch.add(pid)
            new_papers.append(p)
            per_month.setdefault(_month_key(p.published_date), []).append(p)

        if skipped_no_date:
            logger.warning("Skipped %d papers without published_date", skipped_no_date)
        if not new_papers:
            return []

        self.root.mkdir(parents=True, exist_ok=True)
        for ym, batch in per_month.items():
            month_path = self.root / f"{ym}_rolling.jsonl"
            with month_path.open("a", encoding="utf-8") as f:
                for p in batch:
                    f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")
        return new_papers

    def prune(self, today: date, window_days: int = 30) -> int:
        cutoff = today - timedelta(days=window_days)
        cutoff_month = _month_key(cutoff)
        dropped = 0

        for f in self._all_files():
            file_month = f.stem.split("_", 1)[0]
            if file_month < cutoff_month:
                # Whole month before cutoff — drop the whole file.
                with f.open("r", encoding="utf-8") as fp:
                    dropped += sum(1 for line in fp if line.strip())
                f.unlink()
                continue
            if file_month > cutoff_month:
                # Whole month after cutoff — keep as-is.
                continue
            # Cutoff falls inside this month — filter row by row.
            kept: List[Paper] = []
            with f.open("r", encoding="utf-8") as fp:
                total = 0
                for line in fp:
                    line = line.strip()
                    if not line:
                        continue
                    total += 1
                    paper = Paper.from_jsonl_dict(json.loads(line))
                    if paper.published_date and paper.published_date >= cutoff:
                        kept.append(paper)
            dropped += total - len(kept)
            if not kept:
                f.unlink()
            else:
                with f.open("w", encoding="utf-8") as fp:
                    for p in kept:
                        fp.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")
        return dropped
