"""Rolling JSONL metadata database."""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable, List

from .models import Paper


class RollingDB:
    """Append-only JSONL DB with id-based dedup + date-based prune.

    Note: `append` re-reads the whole file on every call (O(n) per call, O(n*m)
    if called m times for chunked input). Fine at current scale (~30k rows);
    if backfill ever calls in tight loops, lift the existing-id set into a
    long-lived caller and skip re-reads.
    """

    def __init__(self, path: Path):
        self.path = Path(path)

    def load_all(self) -> List[Paper]:
        if not self.path.exists():
            return []
        out: List[Paper] = []
        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                out.append(Paper.from_jsonl_dict(json.loads(line)))
        return out

    def append(self, papers: Iterable[Paper]) -> List[Paper]:
        """Append unseen papers; return the list of newly-written papers
        in input order. Dedups against existing rows AND in-batch duplicates."""
        existing_ids = {p.get_id() for p in self.load_all()}
        seen_in_batch: set[str] = set()
        new_papers: List[Paper] = []
        for p in papers:
            pid = p.get_id()
            if pid in existing_ids or pid in seen_in_batch:
                continue
            seen_in_batch.add(pid)
            new_papers.append(p)
        if not new_papers:
            return []
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            for p in new_papers:
                f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")
        return new_papers

    def prune(self, today: date, window_days: int = 30) -> int:
        cutoff = today - timedelta(days=window_days)
        all_papers = self.load_all()
        kept = [p for p in all_papers if p.published_date and p.published_date >= cutoff]
        dropped = len(all_papers) - len(kept)
        if dropped == 0:
            return 0
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            for p in kept:
                f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")
        return dropped
