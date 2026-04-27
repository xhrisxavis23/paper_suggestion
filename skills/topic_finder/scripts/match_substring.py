"""Substring matching of expanded keywords against paper title+abstract."""
from __future__ import annotations

import sys
from datetime import date as _date
from pathlib import Path
from typing import Iterable, List, Optional

# Bootstrap so direct invocation (python scripts/match_substring.py) also works.
_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from collector.src.models import Paper

# Venue weights for I-1 ranking — top-tier venues outrank arXiv-only.
# Higher = better. Unlisted venues default to 0.
_VENUE_WEIGHT = {
    "NeurIPS": 5,
    "ICML": 5,
    "ICLR": 5,
    "CVPR": 5,
    "ICCV": 5,
    "ECCV": 4,
    "ACL": 4,
    "EMNLP": 4,
    "NAACL": 4,
    "AAAI": 3,
    "KDD": 3,
    "HF": 1,
    "arXiv": 0,
}


def _venue_weight(p: Paper) -> int:
    return _VENUE_WEIGHT.get(p.venue or "", 0)


def match_substring(
    papers: Iterable[Paper],
    keywords: List[str],
    *,
    max_papers: Optional[int] = None,
) -> List[Paper]:
    """Return papers where ANY keyword (lowercased) is a substring of
    (title + " " + abstract) lowercased. Deduplicated by id.

    If `max_papers` is set, the result is ranked by (published_date DESC,
    venue_weight DESC) and truncated. This bounds prompt size for the
    downstream 4-bot pipeline (Sonnet 200K context); without a cap, popular
    topics return 2K–6K matches that blow the window.
    """
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
    if max_papers is not None and len(out) > max_papers:
        out.sort(
            key=lambda p: (
                p.published_date or _date.min,
                _venue_weight(p),
            ),
            reverse=True,
        )
        out = out[:max_papers]
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
    parser.add_argument("--max-papers", type=int, default=200,
                        help="Hard cap on returned papers (ranked by date+venue). "
                             "Bounds Sonnet prompt size. Default 200.")
    args = parser.parse_args()

    keywords = json.loads(Path(args.keywords_file).read_text())
    since = (
        date.today() - timedelta(days=args.window_days)
        if args.window_days is not None
        else None
    )
    papers = load_rolling(Path(args.rolling_dir), since=since)
    matched_full = match_substring(papers, keywords)
    matched = match_substring(papers, keywords, max_papers=args.max_papers)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for p in matched:
            f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")

    capped = len(matched_full) > args.max_papers
    suffix = (f" (capped from {len(matched_full)}; ranked by date desc + venue weight)"
              if capped else "")
    print(f"Matched {len(matched)} papers (window={args.window_days}d){suffix} → {args.out}")
