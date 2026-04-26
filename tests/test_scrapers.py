import pytest
from datetime import date

from collector.src.scrapers.arxiv import ArxivScraper
from collector.src.scrapers.huggingface import HuggingFaceScraper


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
