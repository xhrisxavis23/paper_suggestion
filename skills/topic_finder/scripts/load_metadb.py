"""Load the rolling JSONL DB written by the collector."""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from typing import List, Optional

# Make `collector.src.models` importable when this script runs from the skill dir.
_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from collector.src.models import Paper

DEFAULT_ROLLING_PATH = _REPO_ROOT / "metadb" / "rolling.jsonl"


def load_rolling(path: Path | None = None,
                 since: Optional[date] = None) -> List[Paper]:
    """Load papers from the rolling JSONL.

    Args:
        path: jsonl path; defaults to <repo_root>/metadb/rolling.jsonl.
        since: if provided, only papers with published_date >= since are returned.
    """
    path = Path(path) if path is not None else DEFAULT_ROLLING_PATH
    if not path.exists():
        return []
    out: List[Paper] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            paper = Paper.from_jsonl_dict(json.loads(line))
            if since is not None:
                if paper.published_date is None or paper.published_date < since:
                    continue
            out.append(paper)
    return out


if __name__ == "__main__":
    # CLI: dump count for debugging
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    papers = load_rolling(p)
    print(f"{len(papers)} papers in {p or DEFAULT_ROLLING_PATH}")
