"""Journal scraper via OpenAlex.

OpenAlex is free (no API key needed), structured, and the ISSN filter on
`primary_location.source.issn` lets us pull a journal cleanly without
hitting per-publisher quirks.

For each `JOURNAL_TARGETS` entry, fetch papers published since
`target_date − ROLLING_WINDOW_DAYS`, paginate up to `JOURNAL_PER_VENUE_LIMIT`,
and emit `Paper` rows with `source = "openalex"` and `venue` = the journal's
display name. `target_date` is used only as the upper bound — like S2/OR,
journals don't have a meaningful per-day publication cadence at our cadence,
so backfill wires this as a one-shot.
"""
from __future__ import annotations

import logging
import os
import time
from datetime import date, timedelta
from typing import List

import requests

from ..config import (
    JOURNAL_PER_VENUE_LIMIT,
    JOURNAL_TARGETS,
    ROLLING_WINDOW_DAYS,
    USER_AGENT,
)
from ..models import Paper

logger = logging.getLogger(__name__)

OPENALEX_WORKS = "https://api.openalex.org/works"
OPENALEX_PAGE = 50          # OpenAlex default; max 200 with select
OPENALEX_DELAY = 0.5        # courtesy pacing between page fetches
OPENALEX_FIELDS = (
    "id,doi,title,publication_date,authorships,abstract_inverted_index,"
    "primary_location,open_access"
)


def _reconstruct_abstract(inv: dict | None) -> str:
    """OpenAlex returns abstracts as `{word: [positions]}` (inverted index).
    Reverse it to plain text. Null/empty → empty string."""
    if not inv:
        return ""
    pos_word: list[tuple[int, str]] = []
    for word, positions in inv.items():
        for p in positions or []:
            pos_word.append((p, word))
    pos_word.sort(key=lambda t: t[0])
    return " ".join(w for _, w in pos_word)


def _doi_to_id(doi: str | None) -> str | None:
    """Strip the `https://doi.org/` prefix so the id is the bare DOI."""
    if not doi:
        return None
    return doi.replace("https://doi.org/", "").replace("http://doi.org/", "")


class JournalScraper:
    def __init__(self, session: requests.Session | None = None,
                 mailto: str | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        # OpenAlex "polite pool": including `mailto=` lifts the default rate
        # limit. Read from env so CI / cron can opt in.
        self.mailto = mailto or os.environ.get("OPENALEX_MAILTO", "")
        self.failures: List[str] = []

    def fetch(self, target_date: date) -> List[Paper]:
        """target_date is the upper bound; lower bound = target − rolling window."""
        self.failures = []
        out: List[Paper] = []
        cutoff = target_date - timedelta(days=ROLLING_WINDOW_DAYS)
        for tgt in JOURNAL_TARGETS:
            try:
                out.extend(self._fetch_journal(
                    tgt["issn"], tgt["name"], cutoff, target_date))
            except Exception as e:
                logger.warning("journal %s (%s) failed: %s",
                               tgt["name"], tgt["issn"], e)
                self.failures.append(
                    f"openalex:{tgt['name']}:{type(e).__name__}: {e}")
            time.sleep(OPENALEX_DELAY)
        logger.info("journal: %d papers across %d targets",
                    len(out), len(JOURNAL_TARGETS))
        return out

    def _fetch_journal(self, issn: str, venue: str,
                       since: date, until: date) -> List[Paper]:
        """Paginate OpenAlex up to JOURNAL_PER_VENUE_LIMIT."""
        out: List[Paper] = []
        cursor = "*"
        while cursor and len(out) < JOURNAL_PER_VENUE_LIMIT:
            params = {
                # `type:article|review` drops paratext (TOCs, errata,
                # editorials) which OpenAlex still returns by default.
                # `is_paratext:false` is a belt-and-braces guard.
                "filter": (f"primary_location.source.issn:{issn},"
                           f"from_publication_date:{since.isoformat()},"
                           f"to_publication_date:{until.isoformat()},"
                           f"type:article|review,"
                           f"is_paratext:false"),
                "select": OPENALEX_FIELDS,
                "per-page": OPENALEX_PAGE,
                "cursor": cursor,
                "sort": "publication_date:desc",
            }
            if self.mailto:
                params["mailto"] = self.mailto
            r = self.session.get(OPENALEX_WORKS, params=params, timeout=30)
            if r.status_code == 429:
                # OpenAlex rarely rate-limits with mailto; record and stop this venue.
                logger.warning("OpenAlex 429 on %s — backing off", venue)
                self.failures.append(f"openalex:{venue}:rate-limited (429)")
                time.sleep(5)
                break
            r.raise_for_status()
            payload = r.json()
            results = payload.get("results", [])
            if not results:
                break
            for item in results:
                p = self._to_paper(item, venue)
                if p is not None:
                    out.append(p)
                    if len(out) >= JOURNAL_PER_VENUE_LIMIT:
                        break
            cursor = (payload.get("meta") or {}).get("next_cursor")
            time.sleep(OPENALEX_DELAY)
        logger.info("journal %s: %d papers (since %s)", venue, len(out), since)
        return out

    @staticmethod
    def _to_paper(item: dict, venue: str) -> Paper | None:
        title = (item.get("title") or "").strip()
        if not title:
            return None
        abstract = _reconstruct_abstract(item.get("abstract_inverted_index"))
        # Drop non-research artifacts (TOCs, errata stubs, "Corrections to ..."
        # entries). OpenAlex classifies these as type:article so a server-side
        # filter doesn't catch them — empty-abstract is the reliable signal.
        if not abstract:
            return None
        authors = [
            (a.get("author") or {}).get("display_name", "")
            for a in (item.get("authorships") or [])
        ]
        authors = [a for a in authors if a]
        pub_str = item.get("publication_date")
        try:
            pub_date = date.fromisoformat(pub_str) if pub_str else None
        except Exception:
            pub_date = None
        doi = _doi_to_id(item.get("doi"))
        # Prefer OA URL when present (free PDF); else fall back to DOI gateway
        # which paywalled publishers redirect through.
        oa = (item.get("open_access") or {}).get("oa_url") or ""
        prim = (item.get("primary_location") or {})
        landing = prim.get("landing_page_url") or ""
        url = landing or (f"https://doi.org/{doi}" if doi else "")
        # OpenAlex often surfaces `pdf_url` under primary_location for OA works.
        pdf_url = (prim.get("pdf_url") or oa or "").strip()
        return Paper(
            title=title,
            abstract=abstract,
            authors=authors,
            url=url,
            pdf_url=pdf_url,
            arxiv_id=None,
            venue=venue,
            source="openalex",
            published_date=pub_date,
            categories=[],
        )
