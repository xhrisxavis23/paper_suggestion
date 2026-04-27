"""Paper data model + JSONL serialization."""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import date
from typing import List, Optional


@dataclass
class Paper:
    title: str
    abstract: str = ""
    authors: List[str] = field(default_factory=list)
    url: str = ""
    pdf_url: str = ""
    arxiv_id: Optional[str] = None
    venue: Optional[str] = None  # "arXiv", "NeurIPS", "ICLR", ...
    source: str = ""              # primary source: "arxiv" | "hf" | "openreview" | "s2"
    published_date: Optional[date] = None
    # Currently arxiv-only — HF/OpenReview/S2 leave this []. A future
    # category-based filter would silently exclude non-arxiv papers.
    categories: List[str] = field(default_factory=list)
    # Other sources where this paper also appeared (e.g., ["hf"] when an
    # arxiv paper was also on HuggingFace daily). Populated by RollingDB.append
    # on id collision so we don't lose the second-source curation signal.
    also_in: List[str] = field(default_factory=list)

    @property
    def year(self) -> Optional[int]:
        return self.published_date.year if self.published_date else None

    def get_id(self) -> str:
        if self.arxiv_id:
            base = self.arxiv_id.split("v")[0]
            return f"arxiv:{base}"
        normalized = " ".join(self.title.lower().split())
        return f"title:{normalized}"

    def to_jsonl_dict(self) -> dict:
        # We don't emit `id` — readers compute it via get_id() at load time.
        # Persisting it would let an id-formula change silently re-key old rows.
        d = asdict(self)
        d["date"] = self.published_date.isoformat() if self.published_date else None
        d.pop("published_date")
        return d

    @classmethod
    def from_jsonl_dict(cls, d: dict) -> "Paper":
        date_str = d.get("date")
        published = date.fromisoformat(date_str) if date_str else None
        return cls(
            title=d["title"],
            abstract=d.get("abstract", ""),
            authors=list(d.get("authors", [])),
            url=d.get("url", ""),
            pdf_url=d.get("pdf_url", ""),
            arxiv_id=d.get("arxiv_id"),
            venue=d.get("venue"),
            source=d.get("source", ""),
            published_date=published,
            categories=list(d.get("categories", [])),
            also_in=list(d.get("also_in", [])),
        )
