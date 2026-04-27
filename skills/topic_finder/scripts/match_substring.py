"""Substring matching of expanded keywords against paper title+abstract."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, List

# Bootstrap so direct invocation (python scripts/match_substring.py) also works.
_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from collector.src.models import Paper


def match_substring(papers: Iterable[Paper], keywords: List[str]) -> List[Paper]:
    """Return papers where ANY keyword (lowercased) is a substring
    of (title + " " + abstract) lowercased. Order preserved, deduplicated by id."""
    if not keywords:
        return []
    lowered = [k.lower() for k in keywords if k.strip()]
    seen: set[str] = set()
    out: List[Paper] = []
    for p in papers:
        key = p.get_id()
        if key in seen:
            continue
        haystack = f"{p.title} {p.abstract}".lower()
        if any(k in haystack for k in lowered):
            seen.add(key)
            out.append(p)
    return out


if __name__ == "__main__":
    import argparse
    import json
    from datetime import date, timedelta

    from skills.topic_finder.scripts.load_metadb import (
        DEFAULT_ROLLING_DIR,
        load_rolling,
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("--rolling-dir", default=str(DEFAULT_ROLLING_DIR),
                        help="Directory containing <YYMM>_rolling.jsonl files.")
    parser.add_argument("--keywords-file", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--window-days", type=int, default=None,
                        help="Filter to papers with published_date within "
                             "the last N days (relative to today UTC).")
    args = parser.parse_args()

    keywords = json.loads(Path(args.keywords_file).read_text())
    since = (
        date.today() - timedelta(days=args.window_days)
        if args.window_days is not None
        else None
    )
    papers = load_rolling(Path(args.rolling_dir), since=since)
    matched = match_substring(papers, keywords)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for p in matched:
            f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")
    print(f"Matched {len(matched)} papers (window={args.window_days}d) → {args.out}")
