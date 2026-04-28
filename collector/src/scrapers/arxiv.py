"""arXiv scraper — collect ALL papers in configured categories (no topic filter).

Differs from paper_find: no TOPIC_SEARCH_TERMS — query is just per-category
within a date range. Returns every paper arXiv reports for that window.
"""
from __future__ import annotations

import logging
import time
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from typing import List, Tuple

import requests

from ..config import (
    ARXIV_CATEGORIES,
    ARXIV_LOOKBACK_DAYS,
    ARXIV_MAX_RESULTS_PER_CATEGORY,
    USER_AGENT,
)
from ..models import Paper

logger = logging.getLogger(__name__)

ARXIV_API = "http://export.arxiv.org/api/query"
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}
ARXIV_DELAY = 3.0  # API recommends 3-second pacing
# Backoff delays between retries on 429 / 5xx / timeout. Length = max retries.
# Tuned for arXiv — short bursts of 429 typically clear within ~30-60s, longer
# IP throttles can persist a few minutes after heavy backfill.
ARXIV_RETRY_DELAYS = (5, 15, 45, 90)
ARXIV_RETRY_STATUSES = {429, 500, 502, 503, 504}


def _date_window(target: date, lookback: int) -> Tuple[date, date]:
    """Date window with weekend rollback (arXiv has no Sat/Sun submissions)."""
    weekday = target.weekday()  # 0=Mon ... 6=Sun
    if weekday == 0:                                        # Monday
        return target - timedelta(days=lookback + 2), target
    if weekday in (5, 6):                                   # Sat/Sun
        return target - timedelta(days=lookback + (weekday - 4)), target
    return target - timedelta(days=lookback), target


def _result_to_paper(entry: ET.Element, category: str) -> Paper:
    title = (entry.findtext("atom:title", "", NS) or "").strip()
    abstract = (entry.findtext("atom:summary", "", NS) or "").strip()
    authors = [
        (a.findtext("atom:name", "", NS) or "").strip()
        for a in entry.findall("atom:author", NS)
    ]
    arxiv_url = (entry.findtext("atom:id", "", NS) or "").strip()
    arxiv_id = arxiv_url.rsplit("/", 1)[-1] if arxiv_url else None

    published = entry.findtext("atom:published", "", NS) or ""
    try:
        pub_dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
        pub_date = pub_dt.astimezone(timezone.utc).date()
    except Exception:
        pub_date = None

    pdf_url = ""
    for link in entry.findall("atom:link", NS):
        if link.attrib.get("title") == "pdf":
            pdf_url = link.attrib.get("href", "")
            break

    cats = []
    for c in entry.findall("atom:category", NS):
        term = c.attrib.get("term")
        if term and term.startswith(("cs.", "stat.", "math.", "q-")):
            cats.append(term)
    if category not in cats:
        cats.insert(0, category)

    return Paper(
        title=title,
        abstract=abstract,
        authors=authors,
        url=arxiv_url,
        pdf_url=pdf_url,
        arxiv_id=arxiv_id,
        venue="arXiv",
        source="arxiv",
        published_date=pub_date,
        categories=cats,
    )


class ArxivScraper:
    def __init__(self, session: requests.Session | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self.failures: List[str] = []

    def fetch(self, target_date: date) -> List[Paper]:
        self.failures = []
        start, end = _date_window(target_date, ARXIV_LOOKBACK_DAYS)
        out: List[Paper] = []
        for cat in ARXIV_CATEGORIES:
            try:
                out.extend(self._fetch_category(cat, start, end))
            except Exception as e:
                logger.warning("arXiv category %s failed: %s", cat, e)
                self.failures.append(f"arxiv:{cat}:{type(e).__name__}: {e}")
            time.sleep(ARXIV_DELAY)
        logger.info("arXiv: %d papers across %d categories",
                    len(out), len(ARXIV_CATEGORIES))
        return out

    def _fetch_category(self, category: str, start: date, end: date) -> List[Paper]:
        start_str = start.strftime("%Y%m%d") + "0000"
        end_str = end.strftime("%Y%m%d") + "2359"
        query = (
            f"cat:{category} "
            f"AND submittedDate:[{start_str} TO {end_str}]"
        )
        params = {
            "search_query": query,
            "max_results": ARXIV_MAX_RESULTS_PER_CATEGORY,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        # Retry on transient errors (429 / 5xx / timeout). Final failure
        # propagates to the per-category try/except in fetch().
        last_exc: Exception | None = None
        for attempt in range(len(ARXIV_RETRY_DELAYS) + 1):
            if attempt > 0:
                wait = ARXIV_RETRY_DELAYS[attempt - 1]
                logger.info("arXiv %s retry %d/%d after %ds (%s)",
                            category, attempt, len(ARXIV_RETRY_DELAYS), wait,
                            type(last_exc).__name__ if last_exc else "?")
                time.sleep(wait)
            try:
                r = self.session.get(ARXIV_API, params=params, timeout=30)
            except requests.exceptions.Timeout as e:
                last_exc = e
                continue
            if r.status_code in ARXIV_RETRY_STATUSES:
                last_exc = requests.HTTPError(f"{r.status_code} for {r.url}")
                continue
            r.raise_for_status()
            root = ET.fromstring(r.content)
            return [_result_to_paper(e, category) for e in root.findall("atom:entry", NS)]
        # Exhausted retries — surface the last transient error.
        assert last_exc is not None
        raise last_exc
