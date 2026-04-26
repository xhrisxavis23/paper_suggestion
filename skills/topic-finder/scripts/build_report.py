"""Assemble the final Markdown report from 4-bot JSON outputs."""
from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Dict, List, Tuple

from collector.src.models import Paper


def build_report(
    *,
    topic: str,
    expanded: List[str],
    matched: List[Paper],
    clusters: List[dict],
    gaps_validated: Dict[str, List[dict]],
    proposals: List[dict],
    run_meta: dict,
    window: Tuple[date, date],
) -> str:
    by_id = {p.get_id(): p for p in matched}
    out: List[str] = []
    out.append(f'# Research Topic Suggestion — "{topic}"')
    out.append("")
    out.append(f"생성: {datetime.now(timezone.utc).isoformat()}")
    out.append(f"DB 윈도우: {window[0].isoformat()} ~ {window[1].isoformat()} (30d)")
    out.append(f"모델: {run_meta.get('model', 'claude-sonnet-4-6')}")
    out.append(f"매칭 논문: {len(matched)}건")
    out.append(f"확장 키워드: {expanded}")
    out.append("")
    out.append("---")
    out.append("")

    # Section 1 — Trends
    out.append("## 1. 트렌드 요약 (Trend-Analyzer)")
    out.append("")
    for i, c in enumerate(clusters, 1):
        out.append(f"### 클러스터 {i} — {c.get('name', '')}")
        out.append(f"- **설명**: {c.get('description', '')}")
        cnt = c.get("weekly_count", [])
        out.append(f"- **빈도**: {sum(cnt) if cnt else len(c.get('paper_ids', []))}건")
        if cnt:
            out.append(f"- **주차별**: {' → '.join(str(x) for x in cnt)}")
        top3 = c.get("top3", [])[:3]
        if top3:
            out.append("- **대표 논문**:")
            for pid in top3:
                p = by_id.get(pid)
                if p:
                    out.append(f"  - [{_short_id(pid)}] {p.title} — {_authors(p)}, {p.venue or '—'} {p.year or ''}")
        out.append("")

    # Section 2 — Gaps
    out.append("## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)")
    out.append("")
    passed = gaps_validated.get("passed", [])
    rejected = gaps_validated.get("rejected", [])
    for g in passed:
        out.append(f"### Gap {g.get('id')} — {g.get('description', '').splitlines()[0][:80]}")
        out.append(f"- **타입**: {g.get('type', '')}")
        out.append(f"- **설명**: {g.get('description', '')}")
        ev = g.get("evidence_papers", [])
        if ev:
            out.append(f"- **근거 논문**: {', '.join(_short_id(x) for x in ev)}")
        out.append(f"- **Skeptic 검토**: ✓ 통과 — {g.get('skeptic_note', '')}")
        out.append("")
    if rejected:
        out.append("<details>")
        out.append("<summary>검토 후 제외된 갭 (참고용)</summary>")
        out.append("")
        for g in rejected:
            out.append(f"- **Gap {g.get('id')}** — {g.get('description', '')} · 거부 사유: {g.get('reason', '')}")
        out.append("")
        out.append("</details>")
        out.append("")

    # Section 3 — Proposals
    out.append("## 3. 연구 제안 (Proposer)")
    out.append("")
    for prop in proposals:
        out.append(f"### 제안 {prop.get('id')} — {prop.get('name', '')}")
        out.append(f"**가설**: {prop.get('hypothesis', '')}")
        out.append(f"**메우는 갭**: {prop.get('fills_gap', '')}")
        out.append(f"**접근**: {prop.get('approach', '')}")
        out.append(f"**Baselines**: {prop.get('baselines', '')}")
        out.append(f"**예상 기여**: {prop.get('expected_contribution', '')}")
        refs = prop.get("references", [])
        if refs:
            out.append(f"**참고**: {', '.join(_short_id(x) for x in refs)}")
        out.append("")

    # Section 4 — References
    out.append("## 4. 참고문헌 (메타DB 기반)")
    out.append("")
    for p in matched:
        sid = _short_id(p.get_id())
        out.append(f"[{sid}] {p.title}, {_authors(p)}, {p.venue or '—'} {p.year or ''} · {p.url}")
    out.append("")

    # Meta
    out.append("---")
    out.append("")
    out.append("## 메타 / 디버그")
    for k, v in run_meta.items():
        out.append(f"- {k}: {v}")
    out.append("")
    return "\n".join(out)


def _short_id(pid: str) -> str:
    """arxiv:2404.0001 → P-2404.0001 (just for display)."""
    if pid.startswith("arxiv:"):
        return f"P-{pid[6:]}"
    return f"P-{pid[:20]}"


def _authors(p: Paper) -> str:
    if not p.authors:
        return "—"
    if len(p.authors) <= 3:
        return ", ".join(p.authors)
    return f"{', '.join(p.authors[:3])} et al."
