from datetime import date

from collector.src.models import Paper
from skills.topic_finder.scripts.build_report import build_report, _short_id


# ---- M-4: _short_id collision-resistance for non-arxiv papers ----

def test_short_id_arxiv_is_lossless():
    assert _short_id("arxiv:2604.0001", "arXiv") == "P-2604.0001"


def test_short_id_non_arxiv_distinguishes_long_prefix_collisions():
    """Two title-keyed papers sharing a long prefix produce different short ids
    (the v0.1 truncation form would have collided)."""
    a = _short_id("title:a very very long shared prefix that goes on and on but A", "NeurIPS")
    b = _short_id("title:a very very long shared prefix that goes on and on but B", "NeurIPS")
    assert a != b
    assert a.startswith("P-NEURIPS-") and b.startswith("P-NEURIPS-")


def test_short_id_non_arxiv_without_venue_falls_back_to_X():
    sid = _short_id("title:something", venue=None)
    assert sid.startswith("P-X-")


def test_short_id_normalizes_venue_special_chars():
    """Venues like 'Workshop on …' get punctuation stripped before slugging."""
    sid = _short_id("title:foo", venue="Workshop @ NeurIPS-2026")
    # WORKSHOP gets truncated to 8 chars, then capped — first 8 alnum chars uppercased.
    assert sid.startswith("P-WORKSHOP-")


def make_paper(arxiv_id: str, title: str = "T") -> Paper:
    return Paper(title=title, arxiv_id=arxiv_id,
                 published_date=date(2026, 4, 26), source="arxiv",
                 url=f"http://arxiv.org/abs/{arxiv_id}",
                 venue="arXiv", authors=["A"])


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
