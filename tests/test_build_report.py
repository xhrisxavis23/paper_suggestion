from datetime import date

from collector.src.models import Paper
from skills.topic_finder.scripts.build_report import build_report


def make_paper(arxiv_id: str, title: str = "T") -> Paper:
    return Paper(title=title, arxiv_id=arxiv_id,
                 published_date=date(2026, 4, 26), source="arxiv",
                 url=f"http://arxiv.org/abs/{arxiv_id}",
                 venue="arXiv", authors=["A"], year=2026)


def test_build_report_has_all_sections():
    matched = [make_paper("2404.0001"), make_paper("2404.0002")]
    clusters = [{"name": "cluster1", "description": "d", "paper_ids": ["arxiv:2404.0001"],
                 "weekly_count": [1, 2], "top3": ["arxiv:2404.0001"]}]
    gaps_validated = {
        "passed": [{"id": "A", "type": "between-clusters",
                    "description": "g desc", "evidence_papers": ["arxiv:2404.0001"],
                    "skeptic_note": "ok"}],
        "rejected": [{"id": "X", "description": "rejected", "reason": "covered"}],
    }
    proposals = [{"id": 1, "name": "PROPOSAL-A", "fills_gap": "A",
                  "hypothesis": "h", "approach": "a",
                  "baselines": "b", "expected_contribution": "ec",
                  "references": ["arxiv:2404.0001"]}]

    md = build_report(
        topic="LLM safety",
        expanded=["llm safety", "alignment"],
        matched=matched,
        clusters=clusters,
        gaps_validated=gaps_validated,
        proposals=proposals,
        run_meta={"model": "claude-sonnet-4-6", "tokens_in": 100, "tokens_out": 20},
        window=(date(2026, 3, 27), date(2026, 4, 26)),
    )

    assert md.startswith("# Research Topic Suggestion — \"LLM safety\"")
    assert "## 1. 트렌드 요약" in md
    assert "## 2. 갭 분석" in md
    assert "## 3. 연구 제안" in md
    assert "## 4. 참고문헌" in md
    assert "PROPOSAL-A" in md
    assert "<details>" in md  # rejected gaps fold
