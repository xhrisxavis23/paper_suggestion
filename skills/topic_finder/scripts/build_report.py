"""Assemble the final Markdown report from 4-bot JSON outputs."""
from __future__ import annotations

import hashlib
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

# Bootstrap so direct invocation (python scripts/build_report.py) also works.
_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

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
    window_days = (window[1] - window[0]).days
    out.append(f"DB 윈도우: {window[0].isoformat()} ~ {window[1].isoformat()} ({window_days}d)")
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
                    out.append(f"  - [{_short_id(pid, p.venue)}] {p.title} — {_authors(p)}, {p.venue or '—'} {p.year or ''}")
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
            out.append(f"- **근거 논문**: {', '.join(_short_id(x, by_id[x].venue if x in by_id else None) for x in ev)}")
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
            out.append(f"**참고**: {', '.join(_short_id(x, by_id[x].venue if x in by_id else None) for x in refs)}")
        out.append("")

    # Section 4 — References, grouped by cluster (M-11)
    out.append("## 4. 참고문헌 (메타DB 기반)")
    out.append("")
    cluster_order: List[str] = []
    cluster_papers: dict[str, list[Paper]] = {}
    assigned: set[str] = set()
    for i, c in enumerate(clusters, 1):
        name = f"클러스터 {i} — {c.get('name', '')}"
        cluster_order.append(name)
        cluster_papers[name] = []
        for pid in c.get("paper_ids", []) or []:
            if pid in by_id and pid not in assigned:
                cluster_papers[name].append(by_id[pid])
                assigned.add(pid)
    other = [p for p in matched if p.get_id() not in assigned]
    if other:
        cluster_order.append("기타 (클러스터 미분류)")
        cluster_papers["기타 (클러스터 미분류)"] = other

    for cname in cluster_order:
        bucket = cluster_papers[cname]
        if not bucket:
            continue
        out.append(f"### {cname} ({len(bucket)})")
        for p in bucket:
            sid = _short_id(p.get_id(), p.venue)
            also = f" · also_in: {','.join(p.also_in)}" if p.also_in else ""
            out.append(f"- [{sid}] {p.title}, {_authors(p)}, "
                       f"{p.venue or '—'} {p.year or ''} · {p.url}{also}")
        out.append("")

    # Meta
    out.append("---")
    out.append("")
    out.append("## 메타 / 디버그")
    for k, v in run_meta.items():
        out.append(f"- {k}: {v}")
    out.append("")
    return "\n".join(out)


_VENUE_SLUG_RE = re.compile(r"[^A-Za-z0-9]+")


def _short_id(pid: str, venue: str | None = None) -> str:
    """Display-friendly id.

    arxiv:2404.0001 → P-2404.0001 (lossless)
    title:foo bar baz... → P-<venue>-<6-hex of pid> (collision-resistant)
    """
    if pid.startswith("arxiv:"):
        return f"P-{pid[6:]}"
    digest = hashlib.sha1(pid.encode("utf-8")).hexdigest()[:6]
    if venue:
        slug = _VENUE_SLUG_RE.sub("", venue).upper()[:8] or "X"
        return f"P-{slug}-{digest}"
    return f"P-X-{digest}"


def _authors(p: Paper) -> str:
    """First 3 authors verbatim; if more, append ' et al.' (so a paper with
    exactly 3 authors shows all three; 4+ shows three + et al.)."""
    if not p.authors:
        return "—"
    if len(p.authors) <= 3:
        return ", ".join(p.authors)
    return f"{', '.join(p.authors[:3])} et al."


if __name__ == "__main__":
    import argparse
    import json
    from pathlib import Path
    from datetime import date, timedelta

    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--expanded-file", required=True)
    parser.add_argument("--matched-file", required=True)
    parser.add_argument("--clusters-file", required=True)
    parser.add_argument("--gaps-validated-file", required=True)
    parser.add_argument("--proposals-file", required=True)
    parser.add_argument("--window-days", type=int, default=30)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", default="claude-sonnet-4-6")
    args = parser.parse_args()

    expanded = json.loads(Path(args.expanded_file).read_text())
    matched = []
    with open(args.matched_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                matched.append(Paper.from_jsonl_dict(json.loads(line)))
    clusters = json.loads(Path(args.clusters_file).read_text())
    gaps_validated = json.loads(Path(args.gaps_validated_file).read_text())
    proposals = json.loads(Path(args.proposals_file).read_text())

    today = date.today()
    md = build_report(
        topic=args.topic,
        expanded=expanded,
        matched=matched,
        clusters=clusters,
        gaps_validated=gaps_validated,
        proposals=proposals,
        run_meta={"model": args.model},
        window=(today - timedelta(days=args.window_days), today),
    )
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(md, encoding="utf-8")
    print(f"Report → {args.output}")
