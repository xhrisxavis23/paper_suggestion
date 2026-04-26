import pytest
from datetime import date

from collector.src.scrapers.arxiv import ArxivScraper
from collector.src.scrapers.huggingface import HuggingFaceScraper
from collector.src.scrapers.openreview import OpenReviewScraper
from collector.src.scrapers.semantic_scholar import SemanticScholarScraper


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
