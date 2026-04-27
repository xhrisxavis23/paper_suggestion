"""HuggingFace Daily Papers scraper — curated list only (no topic search)."""
from __future__ import annotations

import logging
from datetime import date, timedelta
from typing import List

import requests

from ..config import HF_FALLBACK_DAYS, USER_AGENT
from ..models import Paper

logger = logging.getLogger(__name__)

HF_DAILY_API = "https://huggingface.co/api/daily_papers"


class HuggingFaceScraper:
    def __init__(self, session: requests.Session | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self.failures: List[str] = []

    def fetch(self, target_date: date) -> List[Paper]:
        self.failures = []
        for offset in range(HF_FALLBACK_DAYS + 1):
            d = target_date - timedelta(days=offset)
            papers = self._fetch_one(d)
            if papers:
                logger.info("HF daily %s: %d papers", d, len(papers))
                return papers
        # Exhausted all fallback dates with no papers — record only if HTTP errors
        # occurred (a quiet empty list is normal for some weekend/holiday dates).
        return []

    def _fetch_one(self, d: date) -> List[Paper]:
        try:
            r = self.session.get(
                HF_DAILY_API,
                params={"date": d.isoformat()},
                timeout=30,
            )
            r.raise_for_status()
            data = r.json()
        except Exception as e:
            logger.warning("HF daily %s failed: %s", d, e)
            self.failures.append(f"hf:{d.isoformat()}:{type(e).__name__}: {e}")
            return []
        return [self._parse(item, d) for item in data if "paper" in item]

    @staticmethod
    def _parse(item: dict, fallback_date: date) -> Paper:
        paper = item.get("paper", {})
        arxiv_id = paper.get("id")
        title = (paper.get("title") or "").strip()
        abstract = (paper.get("summary") or "").strip()
        authors = [a.get("name", "") for a in paper.get("authors", []) if a.get("name")]
        return Paper(
            title=title,
            abstract=abstract,
            authors=authors,
            url=f"https://huggingface.co/papers/{arxiv_id}" if arxiv_id else "",
            pdf_url=f"https://arxiv.org/pdf/{arxiv_id}.pdf" if arxiv_id else "",
            arxiv_id=arxiv_id,
            venue="HF",
            year=fallback_date.year,
            source="hf",
            published_date=fallback_date,
            categories=[],
        )
