"""Substring matching of expanded keywords against paper title+abstract."""
from __future__ import annotations

from typing import Iterable, List

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
    from pathlib import Path
    from .load_metadb import load_rolling

    parser = argparse.ArgumentParser()
    parser.add_argument("--rolling", required=True)
    parser.add_argument("--keywords-file", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    keywords = json.loads(Path(args.keywords_file).read_text())
    papers = load_rolling(Path(args.rolling))
    matched = match_substring(papers, keywords)

    with open(args.out, "w", encoding="utf-8") as f:
        for p in matched:
            f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")
    print(f"Matched {len(matched)} papers → {args.out}")
