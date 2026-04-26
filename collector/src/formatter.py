"""Per-day Markdown digest of newly collected metadata."""
from __future__ import annotations

from collections import defaultdict
from datetime import date
from typing import List

from .models import Paper


def format_daily_digest(papers: List[Paper], target_date: date) -> str:
    lines: List[str] = []
    lines.append(f"# Daily metadata digest — {target_date.isoformat()}")
    lines.append("")
    lines.append(f"총 수집: **{len(papers)}건**")
    lines.append("")

    if not papers:
        lines.append("_no papers collected._")
        return "\n".join(lines) + "\n"

    by_source = defaultdict(list)
    for p in papers:
        by_source[p.source or "unknown"].append(p)

    for source in sorted(by_source.keys()):
        bucket = by_source[source]
        lines.append(f"## {source}  ({len(bucket)})")
        lines.append("")
        for p in bucket:
            authors = ", ".join(p.authors[:3]) + (" et al." if len(p.authors) > 3 else "")
            venue_year = f"{p.venue or '—'}"
            if p.year:
                venue_year += f" {p.year}"
            short_abs = (p.abstract or "").strip().replace("\n", " ")
            if len(short_abs) > 200:
                short_abs = short_abs[:200] + "…"
            link = p.url or p.pdf_url or ""
            lines.append(f"- **[{p.title}]({link})** — {authors}")
            lines.append(f"  - {venue_year}")
            if short_abs:
                lines.append(f"  - {short_abs}")
        lines.append("")

    return "\n".join(lines) + "\n"
