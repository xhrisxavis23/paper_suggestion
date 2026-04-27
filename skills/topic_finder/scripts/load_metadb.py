"""Load the monthly-partitioned rolling JSONL DB written by the collector."""
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

DEFAULT_ROLLING_DIR = _REPO_ROOT / "metadb"
ROLLING_GLOB = "*_rolling.jsonl"


def load_rolling(root: Path | None = None,
                 since: Optional[date] = None) -> List[Paper]:
    """Load papers from the monthly rolling JSONL files.

    Args:
        root: directory containing <YYMM>_rolling.jsonl files;
              defaults to <repo_root>/metadb/.
        since: if provided, only papers with published_date >= since are returned.
    """
    root = Path(root) if root is not None else DEFAULT_ROLLING_DIR
    if not root.exists():
        return []
    files = sorted(root.glob(ROLLING_GLOB))
    out: List[Paper] = []
    for path in files:
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
    print(f"{len(papers)} papers in {p or DEFAULT_ROLLING_DIR}")
