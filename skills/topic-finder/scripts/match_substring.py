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
