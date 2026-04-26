"""Load the rolling JSONL DB written by the collector."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List

# Make `collector.src.models` importable when this script runs from the skill dir.
_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from collector.src.models import Paper


def load_rolling(path: Path) -> List[Paper]:
    path = Path(path)
    if not path.exists():
        return []
    out: List[Paper] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(Paper.from_jsonl_dict(json.loads(line)))
    return out


if __name__ == "__main__":
    # CLI: dump count for debugging
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("metadb/rolling.jsonl")
    papers = load_rolling(p)
    print(f"{len(papers)} papers in {p}")
