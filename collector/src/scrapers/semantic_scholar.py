"""Semantic Scholar scraper — recent papers per configured venue."""
from __future__ import annotations

import logging
import os
import time
from datetime import date, timedelta
from typing import List

import requests

from ..config import ROLLING_WINDOW_DAYS, S2_VENUES, USER_AGENT
from ..models import Paper

logger = logging.getLogger(__name__)

S2_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
S2_FIELDS = "title,abstract,authors,venue,year,publicationDate,externalIds,url"
S2_DELAY = 1.0  # courtesy pacing


class SemanticScholarScraper:
    def __init__(self, session: requests.Session | None = None,
                 api_key: str | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        key = api_key or os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
        if key:
            self.session.headers.update({"x-api-key": key})

    def fetch(self, target_date: date) -> List[Paper]:
        out: List[Paper] = []
        cutoff = target_date - timedelta(days=ROLLING_WINDOW_DAYS)
        for venue in S2_VENUES:
            try:
                out.extend(self._fetch_venue(venue, cutoff, target_date))
            except Exception as e:
                logger.warning("S2 venue %s failed: %s", venue, e)
            time.sleep(S2_DELAY)
        logger.info("S2: %d papers across %d venues", len(out), len(S2_VENUES))
        return out

    def _fetch_venue(self, venue: str, since: date, until: date) -> List[Paper]:
        params = {
            "query": venue,
            "venue": venue,
            "publicationDateOrYear": f"{since.isoformat()}:{until.isoformat()}",
            "fields": S2_FIELDS,
            "limit": 100,
        }
        r = self.session.get(S2_SEARCH, params=params, timeout=30)
        if r.status_code == 429:
            logger.warning("S2 rate-limited at venue %s — backing off", venue)
            time.sleep(5)
            return []
        r.raise_for_status()
        data = r.json().get("data", [])

        out: List[Paper] = []
        for item in data:
            title = (item.get("title") or "").strip()
            if not title:
                continue
            abstract = (item.get("abstract") or "").strip()
            authors = [a.get("name", "") for a in item.get("authors", []) if a.get("name")]
            year = item.get("year")
            pub_str = item.get("publicationDate")
            try:
                pub_date = date.fromisoformat(pub_str) if pub_str else None
            except Exception:
                pub_date = None
            ext = item.get("externalIds") or {}
            arxiv_id = ext.get("ArXiv")
            url = item.get("url", "")
            out.append(Paper(
                title=title,
                abstract=abstract,
                authors=authors,
                url=url,
                pdf_url=f"https://arxiv.org/pdf/{arxiv_id}.pdf" if arxiv_id else "",
                arxiv_id=arxiv_id,
                venue=venue,
                year=year,
                source="s2",
                published_date=pub_date,
                categories=[],
            ))
        return out
