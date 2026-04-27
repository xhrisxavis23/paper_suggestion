import json
from datetime import date
from unittest.mock import MagicMock

import pytest

from collector.src.scrapers.arxiv import ArxivScraper, _date_window
from collector.src.scrapers.huggingface import HuggingFaceScraper
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
