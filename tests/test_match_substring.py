from datetime import date

from collector.src.models import Paper
from skills.topic_finder.scripts.match_substring import match_substring


def make(title: str, abstract: str = "", arxiv_id: str = "x") -> Paper:
    return Paper(title=title, abstract=abstract, arxiv_id=arxiv_id,
                 published_date=date(2026, 4, 26), source="arxiv")


def test_match_substring_matches_title():
    papers = [make("LLM jailbreak attacks", arxiv_id="1"),
              make("Image classification", arxiv_id="2")]
    matched = match_substring(papers, ["jailbreak"])
    assert len(matched) == 1
    assert matched[0].arxiv_id == "1"


def test_match_substring_matches_abstract():
    papers = [make("Foo", abstract="adversarial prompt injection", arxiv_id="1")]
    matched = match_substring(papers, ["prompt injection"])
    assert len(matched) == 1


def test_match_substring_case_insensitive():
    papers = [make("LLM Safety", arxiv_id="1")]
    matched = match_substring(papers, ["llm safety"])
    assert len(matched) == 1


def test_match_substring_dedupes_papers():
    p = make("Multi-Agent Coordination", arxiv_id="1")
    matched = match_substring([p], ["multi-agent", "coordination"])
    assert len(matched) == 1


def test_match_substring_returns_empty_when_no_match():
    papers = [make("Foo", arxiv_id="1")]
    assert match_substring(papers, ["bar"]) == []


# I-1: max_papers ranking + cap
def test_match_substring_max_papers_caps_by_venue_then_date():
    from datetime import date as _d
    from collector.src.models import Paper

    fresh_arxiv = Paper(title="A latest", arxiv_id="1",
                        published_date=_d(2026, 4, 20), source="arxiv", venue="arXiv")
    older_neurips = Paper(title="A older nips", arxiv_id="2",
                          published_date=_d(2026, 4, 15), source="arxiv", venue="NeurIPS")
    older_arxiv = Paper(title="A older arxiv", arxiv_id="3",
                        published_date=_d(2026, 4, 15), source="arxiv", venue="arXiv")
    oldest = Paper(title="A oldest", arxiv_id="4",
                   published_date=_d(2026, 3, 1), source="arxiv", venue="arXiv")

    out = match_substring([fresh_arxiv, older_neurips, older_arxiv, oldest],
                          ["a"], max_papers=3)
    # venue_weight DESC: NeurIPS (weight 5) outranks arXiv (weight 2);
    # within arXiv-tier, date DESC keeps fresh_arxiv (04-20) over older_arxiv (04-15);
    # oldest (03-01) drops off.
    assert [p.arxiv_id for p in out] == ["2", "1", "3"]


def test_match_substring_no_max_papers_preserves_input_order():
    from datetime import date as _d
    from collector.src.models import Paper

    a = Paper(title="A first input", arxiv_id="1",
              published_date=_d(2026, 1, 1), source="arxiv")
    b = Paper(title="A second input", arxiv_id="2",
              published_date=_d(2026, 4, 1), source="arxiv")  # newer but listed second
    out = match_substring([a, b], ["a"])
    # No cap → input order preserved (no sorting)
    assert [p.arxiv_id for p in out] == ["1", "2"]
