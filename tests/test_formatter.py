from datetime import date

from collector.src.models import Paper
from collector.src.formatter import format_daily_digest


def test_daily_digest_has_header_and_groups_by_source():
    today = date(2026, 4, 26)
    papers = [
        Paper(title="Arxiv One", authors=["A"], arxiv_id="2404.0001",
              source="arxiv", venue="arXiv", published_date=today,
              abstract="Short abstract.", url="http://arxiv.org/abs/2404.0001"),
        Paper(title="HF One", authors=["B"], source="hf", venue="HF",
              published_date=today, abstract="HF abstract.",
              url="http://hf.co/x"),
    ]
    md = format_daily_digest(papers, target_date=today)

    assert md.startswith("# Daily metadata digest — 2026-04-26")
    assert "## arxiv" in md
    assert "## hf" in md
    assert "Arxiv One" in md
    assert "HF One" in md


def test_daily_digest_handles_empty_input():
    md = format_daily_digest([], target_date=date(2026, 4, 26))
    assert "no papers collected" in md.lower()
