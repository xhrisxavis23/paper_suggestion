"""Rolling JSONL metadata database, partitioned by month.

On-disk layout:

    <root>/
        2602_rolling.jsonl
        2603_rolling.jsonl
        2604_rolling.jsonl
        ...
        .lock                       # advisory lock for concurrent writers

Each file holds papers whose `published_date` falls in that calendar month
(YY = last two digits of year, MM = month). Splitting keeps individual files
under GitHub's 50 MB recommendation and bounds rewrites on prune.
"""
from __future__ import annotations

import contextlib
import fcntl
import json
import logging
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable, List

from .models import Paper

logger = logging.getLogger(__name__)

ROLLING_GLOB = "*_rolling.jsonl"
LOCK_FILENAME = ".lock"


def _month_key(d: date) -> str:
    return d.strftime("%y%m")


@contextlib.contextmanager
def _flock(lock_path: Path):
    """Advisory exclusive lock on lock_path; releases on context exit.

    Concurrent collector runs (e.g., manual + cron overlap) serialize at this
    point. Lock file is created if missing.
    """
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    fd = lock_path.open("a+")
    try:
        fcntl.flock(fd.fileno(), fcntl.LOCK_EX)
        yield
    finally:
        fcntl.flock(fd.fileno(), fcntl.LOCK_UN)
        fd.close()


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

    def _lock_path(self) -> Path:
        return self.root / LOCK_FILENAME

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

        On id collision with a different source, the existing row's `also_in`
        is augmented with the new source slug (so an arxiv paper later seen
        on HF gets `also_in=["hf"]`). Affected month files are rewritten in
        place to persist the augmentation.

        Papers with no `published_date` are skipped (no monthly bucket).
        """
        with _flock(self._lock_path()):
            existing_by_id: dict[str, tuple[Paper, Path]] = {}
            for f in self._all_files():
                with f.open("r", encoding="utf-8") as fp:
                    for line in fp:
                        line = line.strip()
                        if not line:
                            continue
                        p = Paper.from_jsonl_dict(json.loads(line))
                        existing_by_id[p.get_id()] = (p, f)

            seen_in_batch: set[str] = set()
            new_papers: List[Paper] = []
            per_month: dict[str, List[Paper]] = {}
            dirty_files: set[Path] = set()
            skipped_no_date = 0

            for p in papers:
                pid = p.get_id()
                if pid in seen_in_batch:
                    continue
                if pid in existing_by_id:
                    existing_p, existing_path = existing_by_id[pid]
                    if (
                        p.source
                        and p.source != existing_p.source
                        and p.source not in existing_p.also_in
                    ):
                        existing_p.also_in.append(p.source)
                        dirty_files.add(existing_path)
                    continue
                if p.published_date is None:
                    skipped_no_date += 1
                    continue
                seen_in_batch.add(pid)
                new_papers.append(p)
                per_month.setdefault(_month_key(p.published_date), []).append(p)

            if skipped_no_date:
                logger.warning("Skipped %d papers without published_date",
                               skipped_no_date)

            # Rewrite dirty months in place so also_in mutations persist.
            for path in dirty_files:
                rows: List[Paper] = []
                with path.open("r", encoding="utf-8") as fp:
                    for line in fp:
                        line = line.strip()
                        if not line:
                            continue
                        p = Paper.from_jsonl_dict(json.loads(line))
                        # Use the (possibly mutated) version from the index.
                        p = existing_by_id[p.get_id()][0]
                        rows.append(p)
                with path.open("w", encoding="utf-8") as fp:
                    for p in rows:
                        fp.write(json.dumps(p.to_jsonl_dict(),
                                            ensure_ascii=False) + "\n")

            if not new_papers:
                return []

            self.root.mkdir(parents=True, exist_ok=True)
            for ym, batch in per_month.items():
                month_path = self.root / f"{ym}_rolling.jsonl"
                with month_path.open("a", encoding="utf-8") as f:
                    for p in batch:
                        f.write(json.dumps(p.to_jsonl_dict(),
                                           ensure_ascii=False) + "\n")
            return new_papers

    def prune(self, today: date, window_days: int = 30) -> int:
        cutoff = today - timedelta(days=window_days)
        cutoff_month = _month_key(cutoff)
        dropped = 0

        with _flock(self._lock_path()):
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
                            fp.write(json.dumps(p.to_jsonl_dict(),
                                                ensure_ascii=False) + "\n")
        return dropped
