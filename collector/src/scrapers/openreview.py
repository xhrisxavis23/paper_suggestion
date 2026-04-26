"""OpenReview scraper — submissions for active venues, no topic filter."""
from __future__ import annotations

import logging
from datetime import date, datetime, timezone
from typing import List

import requests

from ..config import OPENREVIEW_VENUE_IDS, USER_AGENT
from ..models import Paper

logger = logging.getLogger(__name__)

OR_API = "https://api2.openreview.net/notes"


class OpenReviewScraper:
    def __init__(self, session: requests.Session | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})

    def fetch(self, target_date: date) -> List[Paper]:
        out: List[Paper] = []
        for venue_id in OPENREVIEW_VENUE_IDS:
            try:
                out.extend(self._fetch_venue(venue_id))
            except Exception as e:
                logger.warning("OpenReview %s failed: %s", venue_id, e)
        logger.info("OpenReview: %d papers across %d venues",
                    len(out), len(OPENREVIEW_VENUE_IDS))
        return out

    def _fetch_venue(self, venue_id: str) -> List[Paper]:
        params = {
            "content.venueid": venue_id,
            "limit": 1000,
            "details": "replyCount",
        }
        r = self.session.get(OR_API, params=params, timeout=30)
        r.raise_for_status()
        notes = r.json().get("notes", [])

        out: List[Paper] = []
        venue_short = venue_id.split("/")[0].split(".")[0]
        for n in notes:
            content = n.get("content", {})
            title = (content.get("title", {}) or {}).get("value", "").strip()
            if not title:
                continue
            abstract = (content.get("abstract", {}) or {}).get("value", "").strip()
            authors = (content.get("authors", {}) or {}).get("value", []) or []

            ts_ms = n.get("cdate") or n.get("tcdate")
            pub_date = (
                datetime.fromtimestamp(ts_ms / 1000, tz=timezone.utc).date()
                if ts_ms else None
            )

            forum_id = n.get("forum") or n.get("id")
            url = f"https://openreview.net/forum?id={forum_id}" if forum_id else ""
            pdf_url = f"https://openreview.net/pdf?id={forum_id}" if forum_id else ""

            out.append(Paper(
                title=title,
                abstract=abstract,
                authors=list(authors),
                url=url,
                pdf_url=pdf_url,
                arxiv_id=None,
                venue=venue_short,
                year=pub_date.year if pub_date else None,
                source="openreview",
                published_date=pub_date,
                categories=[],
            ))
        return out
