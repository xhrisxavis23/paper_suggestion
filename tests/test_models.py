from datetime import date
from collector.src.models import Paper


def test_paper_get_id_uses_arxiv_id_when_present():
    p = Paper(title="X", arxiv_id="2404.12345v2")
    assert p.get_id() == "arxiv:2404.12345"


def test_paper_get_id_falls_back_to_normalized_title():
    p = Paper(title="  Foo   Bar  ")
    assert p.get_id() == "title:foo bar"


def test_paper_to_jsonl_dict_roundtrip():
    p = Paper(
        title="Sample",
        abstract="abs",
        authors=["Alice", "Bob"],
        url="http://x",
        arxiv_id="2404.0001",
        venue="arXiv",
        published_date=date(2026, 4, 26),
        source="arxiv",
        categories=["cs.LG", "cs.AI"],
    )
    d = p.to_jsonl_dict()
    assert d["id"] == "arxiv:2404.0001"
    assert d["date"] == "2026-04-26"
    assert d["categories"] == ["cs.LG", "cs.AI"]


def test_paper_from_jsonl_dict_roundtrip():
    p1 = Paper(
        title="Sample",
        abstract="abs",
        authors=["Alice"],
        arxiv_id="2404.0001",
        published_date=date(2026, 4, 26),
        source="arxiv",
    )
    d = p1.to_jsonl_dict()
    p2 = Paper.from_jsonl_dict(d)
    assert p2.title == p1.title
    assert p2.arxiv_id == p1.arxiv_id
    assert p2.published_date == p1.published_date
