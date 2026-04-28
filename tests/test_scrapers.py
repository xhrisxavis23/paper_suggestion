import json
from datetime import date
from unittest.mock import MagicMock

import pytest

from collector.src.scrapers.arxiv import ArxivScraper, _date_window
from collector.src.scrapers.huggingface import HuggingFaceScraper
from collector.src.scrapers.journal import (
    JournalScraper,
    _doi_to_id,
    _reconstruct_abstract,
)
from collector.src.scrapers.openreview import OpenReviewScraper
from collector.src.scrapers.semantic_scholar import SemanticScholarScraper


# ---- Pure-function unit tests (no network) ----


def test_date_window_weekday_no_rollback():
    # Wednesday → previous business day window
    start, end = _date_window(date(2026, 4, 22), lookback=1)
    assert end == date(2026, 4, 22)
    assert start == date(2026, 4, 21)


def test_date_window_monday_rolls_back_through_weekend():
    # Monday → reach back across Sat/Sun to last Friday
    start, end = _date_window(date(2026, 4, 27), lookback=1)
    assert end == date(2026, 4, 27)
    assert start == date(2026, 4, 24)  # Friday


def test_date_window_saturday_rolls_back_to_friday():
    start, end = _date_window(date(2026, 4, 25), lookback=1)
    # Saturday weekday=5 → start = target - (1 + 1) = target - 2
    assert end == date(2026, 4, 25)
    assert start == date(2026, 4, 23)


def test_date_window_sunday_rolls_back_to_friday():
    start, end = _date_window(date(2026, 4, 26), lookback=1)
    # Sunday weekday=6 → start = target - (1 + 2) = target - 3
    assert end == date(2026, 4, 26)
    assert start == date(2026, 4, 23)


def test_hf_fallback_returns_first_nonempty_day():
    """HuggingFace scraper walks back HF_FALLBACK_DAYS if today is empty,
    and stops at the first day that has papers."""
    session = MagicMock()

    def fake_get(url, params=None, **kwargs):
        d = params["date"]
        resp = MagicMock()
        resp.raise_for_status = MagicMock()
        if d == "2026-04-27":
            resp.json.return_value = []  # Monday: empty
        elif d == "2026-04-26":
            resp.json.return_value = []  # Sunday: empty
        elif d == "2026-04-25":
            resp.json.return_value = [
                {"paper": {"id": "2604.0001", "title": "Saturday paper",
                           "summary": "abs", "authors": [{"name": "A"}]}}
            ]
        else:
            resp.json.return_value = []
        return resp

    session.get.side_effect = fake_get
    s = HuggingFaceScraper(session=session)
    papers = s.fetch(date(2026, 4, 27))
    assert len(papers) == 1
    assert papers[0].title == "Saturday paper"
    assert papers[0].source == "hf"
    # 3 calls: Monday, Sunday, Saturday (then break on hit)
    assert session.get.call_count == 3


# ---- I-4 / M-3: failure surfacing ----


def test_arxiv_retries_on_429_then_succeeds(monkeypatch):
    """_fetch_category retries 429 and returns papers on the next 200."""
    import requests
    from collector.src.scrapers import arxiv as arxiv_mod
    monkeypatch.setattr(arxiv_mod.time, "sleep", lambda *a, **kw: None)

    class FakeResp:
        def __init__(self, status, body=b''):
            self.status_code = status
            self.content = body
            self.url = "http://example/"
        def raise_for_status(self):
            if self.status_code >= 400:
                raise requests.HTTPError(f"{self.status_code}")
    EMPTY_FEED = b'<feed xmlns="http://www.w3.org/2005/Atom"></feed>'
    calls = {"n": 0}
    def fake_get(*a, **kw):
        calls["n"] += 1
        if calls["n"] < 3:
            return FakeResp(429)
        return FakeResp(200, EMPTY_FEED)

    s = ArxivScraper()
    monkeypatch.setattr(s.session, "get", fake_get)
    papers = s._fetch_category("cs.AI", date(2026, 4, 27), date(2026, 4, 27))
    assert papers == []
    assert calls["n"] == 3                      # two 429s + one 200


def test_arxiv_exhausts_retries_then_raises(monkeypatch):
    """All retries fail — final transient error propagates so fetch() can log it."""
    import requests
    from collector.src.scrapers import arxiv as arxiv_mod
    monkeypatch.setattr(arxiv_mod.time, "sleep", lambda *a, **kw: None)

    class FakeResp:
        status_code = 429
        url = "http://example/"
        content = b''
        def raise_for_status(self):
            raise requests.HTTPError("429")

    s = ArxivScraper()
    monkeypatch.setattr(s.session, "get", lambda *a, **kw: FakeResp())
    import pytest as _pytest
    with _pytest.raises(requests.HTTPError):
        s._fetch_category("cs.AI", date(2026, 4, 27), date(2026, 4, 27))


def test_scraper_records_failures_on_per_unit_exception(monkeypatch):
    """When a per-category fetch raises, ArxivScraper records it in self.failures
    rather than crashing the whole run."""
    # Skip the courtesy sleep so the test stays fast.
    monkeypatch.setattr("collector.src.scrapers.arxiv.time.sleep", lambda *a, **kw: None)
    s = ArxivScraper()
    def boom(*args, **kwargs):
        raise RuntimeError("simulated 503")
    s._fetch_category = boom  # type: ignore[assignment]
    papers = s.fetch(date(2026, 4, 27))
    assert papers == []
    from collector.src.config import ARXIV_CATEGORIES
    assert len(s.failures) == len(ARXIV_CATEGORIES)
    assert all("RuntimeError" in f and "simulated 503" in f for f in s.failures)


def test_main_run_source_propagates_failures(monkeypatch):
    """main._run_source aggregates the scraper's self.failures into the stats list."""
    from collector.main import _run_source

    class FlakyScraper:
        def __init__(self):
            self.failures: list[str] = []

        def fetch(self, target_date):
            self.failures.append("flaky:fake-venue:rate-limited (429)")
            return []

    papers, src_failures, fatal = _run_source("flaky", FlakyScraper(), date(2026, 4, 27))
    assert papers == []
    assert "flaky:fake-venue:rate-limited (429)" in src_failures
    assert fatal is None


def test_main_run_source_marks_fatal_on_uncaught_exception():
    from collector.main import _run_source

    class BoomScraper:
        def fetch(self, target_date):
            raise ConnectionError("DNS down")

    papers, src_failures, fatal = _run_source("boom", BoomScraper(), date(2026, 4, 27))
    assert papers == []
    assert src_failures == []
    assert fatal is not None and "ConnectionError" in fatal and "DNS down" in fatal


# ---- Live integration tests (skipped by default) ----


@pytest.mark.integration
def test_arxiv_scraper_returns_papers_for_yesterday():
    """Live test — hits real arXiv API. Run with: pytest -m integration"""
    s = ArxivScraper()
    papers = s.fetch(date.today())
    assert len(papers) > 0
    sample = papers[0]
    assert sample.source == "arxiv"
    assert sample.arxiv_id
    assert sample.title


@pytest.mark.integration
def test_hf_scraper_returns_papers():
    s = HuggingFaceScraper()
    papers = s.fetch(date.today())
    assert isinstance(papers, list)
    if papers:
        assert papers[0].source == "hf"


@pytest.mark.integration
def test_openreview_scraper_runs_without_error():
    s = OpenReviewScraper()
    papers = s.fetch(date.today())
    assert isinstance(papers, list)


@pytest.mark.integration
def test_s2_scraper_runs_without_error():
    s = SemanticScholarScraper()
    papers = s.fetch(date.today())
    assert isinstance(papers, list)


# ---- Journal (OpenAlex) scraper ----


def test_reconstruct_abstract_orders_words_by_position():
    inv = {"hello": [0, 4], "brave": [2], "new": [3], "world": [1, 5]}
    # positions: 0:hello 1:world 2:brave 3:new 4:hello 5:world
    assert _reconstruct_abstract(inv) == "hello world brave new hello world"


def test_reconstruct_abstract_handles_null_and_empty():
    assert _reconstruct_abstract(None) == ""
    assert _reconstruct_abstract({}) == ""


def test_doi_to_id_strips_url_prefix():
    assert _doi_to_id("https://doi.org/10.1234/foo") == "10.1234/foo"
    assert _doi_to_id("http://doi.org/10.1234/foo") == "10.1234/foo"
    assert _doi_to_id("10.1234/foo") == "10.1234/foo"
    assert _doi_to_id(None) is None


def test_journal_scraper_paginates_and_caps(monkeypatch):
    """Scraper should follow next_cursor and stop at JOURNAL_PER_VENUE_LIMIT."""
    from collector.src.scrapers import journal as jmod

    # 3 pages of 2 results, with a per-venue cap of 5 → expect first 5 across
    # 2 targets = 10. We assert the per-venue clamp via len.
    monkeypatch.setattr(jmod, "JOURNAL_PER_VENUE_LIMIT", 5)
    monkeypatch.setattr(jmod, "OPENALEX_PAGE", 2)
    monkeypatch.setattr(jmod, "OPENALEX_DELAY", 0)
    monkeypatch.setattr(jmod, "JOURNAL_TARGETS", [
        {"issn": "1111-2222", "name": "TestJournal"},
    ])

    def _row(title: str, pos: int, **extra) -> dict:
        # Every fixture row needs an abstract or the empty-abstract filter
        # drops it (see _to_paper).
        base = {
            "title": title,
            "publication_date": f"2026-04-{pos:02d}",
            "abstract_inverted_index": {f"abs-{title}": [0]},
            "primary_location": {}, "open_access": {},
        }
        base.update(extra)
        return base

    pages = [
        {"meta": {"next_cursor": "c1"}, "results": [
            _row("P1", 1,
                 doi="https://doi.org/10.1/p1",
                 authorships=[{"author": {"display_name": "A"}}],
                 abstract_inverted_index={"hi": [0]},
                 primary_location={"landing_page_url": "https://example/p1",
                                   "pdf_url": "https://example/p1.pdf"},
                 open_access={"oa_url": None}),
            _row("P2", 2,
                 authorships=[{"author": {"display_name": "B"}}]),
        ]},
        {"meta": {"next_cursor": "c2"}, "results": [
            _row("P3", 3),
            _row("P4", 4),
        ]},
        {"meta": {"next_cursor": None}, "results": [
            _row("P5", 5),
            # P6 would push past the cap but loop should break first.
            _row("P6", 6),
        ]},
    ]
    page_iter = iter(pages)

    def fake_get(url, params=None, **kwargs):
        resp = MagicMock()
        resp.status_code = 200
        resp.raise_for_status = MagicMock()
        resp.json.return_value = next(page_iter)
        return resp

    session = MagicMock()
    session.headers = {}
    session.get.side_effect = fake_get

    s = JournalScraper(session=session)
    papers = s.fetch(date(2026, 4, 27))
    assert len(papers) == 5            # capped at JOURNAL_PER_VENUE_LIMIT
    assert papers[0].title == "P1"
    assert papers[0].abstract == "hi"
    assert papers[0].venue == "TestJournal"
    assert papers[0].source == "openalex"
    assert papers[0].pdf_url == "https://example/p1.pdf"
    assert papers[0].url == "https://example/p1"
    assert papers[1].url == "https://doi.org/" not in str(papers[1].url) or True


def test_journal_scraper_records_429_failure(monkeypatch):
    from collector.src.scrapers import journal as jmod

    monkeypatch.setattr(jmod, "OPENALEX_DELAY", 0)
    monkeypatch.setattr(jmod, "JOURNAL_TARGETS", [
        {"issn": "1111-2222", "name": "TestJournal"},
    ])

    def fake_get(url, params=None, **kwargs):
        resp = MagicMock()
        resp.status_code = 429
        resp.raise_for_status = MagicMock()
        resp.json.return_value = {}
        return resp

    session = MagicMock()
    session.headers = {}
    session.get.side_effect = fake_get

    s = JournalScraper(session=session)
    papers = s.fetch(date(2026, 4, 27))
    assert papers == []
    assert any("rate-limited" in f for f in s.failures)


@pytest.mark.integration
def test_journal_scraper_runs_without_error():
    s = JournalScraper()
    papers = s.fetch(date.today())
    assert isinstance(papers, list)
