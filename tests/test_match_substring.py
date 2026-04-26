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
