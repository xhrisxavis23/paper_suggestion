"""PDF body fetch + section extraction for /find-topic --deep (v0.4 I-1).

The 4-bot pipeline normally only sees title + abstract per paper. With
--deep, we additionally pull the PDF for the top-K matched papers, extract
intro / method / limitations sections, and feed that into Skeptic + Proposer
so their gap-validation and proposal grounding has access to method-level
detail that abstracts skip.

Decisions (per v0.4 backlog I-1):
  - Library: pypdf (pure Python, no compile, fine for arxiv-LaTeX PDFs).
  - Sections: regex-based heuristic. Most arxiv papers use numbered or
    capitalized headings — we look for "1. Introduction" / "Introduction" /
    "INTRODUCTION", with similar patterns for Method / Limitations.
    On miss, we fall back to a head-and-tail slice (first ~6K chars +
    last ~2K) which usually covers intro + conclusion / limitations.
  - Cache: metadb/.pdfs/<id-hash>.json — PDF text is immutable per paper
    id, so caching is safe forever; pruned alongside the rolling DB window
    by the existing collector prune step.
  - Failure mode: graceful skip. Any one paper's fetch / extract failure
    drops that paper from the deep_context but does not abort the run.

Usage:
    from skills.topic_finder.scripts.pdf_extract import build_deep_context
    text = build_deep_context(papers[:10], cache_dir="metadb/.pdfs")
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import time
from pathlib import Path
from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from collector.src.models import Paper

CACHE_DIR_DEFAULT = Path("metadb/.pdfs")
PDF_TIMEOUT_SECONDS = 30
PDF_MAX_BYTES = 20_000_000  # 20MB — drop anything larger; tail-bloated PDFs
USER_AGENT = "paper_suggestion/0.4 (find-topic --deep)"

# Per-section character budgets after extraction. Tuned so K=10 papers
# × ~3K chars/paper = ~30K chars ≈ ~7-8K tokens added to Skeptic+Proposer.
INTRO_CHARS = 1500
METHOD_CHARS = 1500
LIMITS_CHARS = 1500
FALLBACK_HEAD = 6000
FALLBACK_TAIL = 2000

# Heading regexes — case-insensitive, optional section numbering, and crucially
# *line-terminated* (the keyword must be at end-of-line allowing only short
# trailing punctuation/whitespace) so prose like "Our approach fails when X."
# does not match _RE_METHOD as if it were a heading.
_HEAD_TAIL = r"[^a-zA-Z0-9\n]{0,20}(?=\n|$)"
_HEAD_PRE = r"(?:^|\n)[ \t]*(?:\d+(?:\.\d+)*\s*[.)]?\s*)?"
_RE_INTRO = re.compile(
    _HEAD_PRE + r"(introduction|background)\b" + _HEAD_TAIL,
    re.IGNORECASE,
)
_RE_METHOD = re.compile(
    _HEAD_PRE
    + r"(method|methods|methodology|proposed method|our approach|"
      r"the proposed approach|model|architecture)\b"
    + _HEAD_TAIL,
    re.IGNORECASE,
)
_RE_LIMITS = re.compile(
    _HEAD_PRE
    + r"(limitations?|threats?\s+to\s+validity|discussion|conclusion(?:s)?)\b"
    + _HEAD_TAIL,
    re.IGNORECASE,
)
# References / appendix markers — used to truncate body content. Same
# line-anchored shape as the section regexes.
_RE_REFS = re.compile(
    _HEAD_PRE
    + r"(references|bibliography|acknowledg(?:e)?ments?|appendix)\b"
    + _HEAD_TAIL,
    re.IGNORECASE,
)


def _cache_key(paper_id: str) -> str:
    """Stable filesystem-safe key for any paper id (arxiv:..., title:...)."""
    if paper_id.startswith("arxiv:"):
        return paper_id[6:].replace("/", "-")
    return "h-" + hashlib.sha1(paper_id.encode("utf-8")).hexdigest()[:16]


def _cache_path(paper_id: str, cache_dir: Path) -> Path:
    return cache_dir / (_cache_key(paper_id) + ".json")


def _pdf_path(paper_id: str, cache_dir: Path) -> Path:
    """Raw PDF bytes lives next to the extracted-sections JSON, same key."""
    return cache_dir / (_cache_key(paper_id) + ".pdf")


def _strip_after_refs(text: str) -> str:
    """Truncate text at the first References / Bibliography / Appendix
    heading we find — body content rarely lives past those."""
    m = _RE_REFS.search(text)
    return text[:m.start()] if m else text


def _slice_section(text: str, head_re: re.Pattern, budget: int) -> str:
    """Return up to `budget` chars starting at the first heading match;
    stop early at the next heading among intro/method/limits/refs."""
    m = head_re.search(text)
    if not m:
        return ""
    start = m.start()
    end = start + budget
    # Stop at the first "next" heading after our match — whichever comes first.
    cut = end
    for nxt_re in (_RE_INTRO, _RE_METHOD, _RE_LIMITS, _RE_REFS):
        nxt = nxt_re.search(text, m.end())
        if nxt and nxt.start() < cut:
            cut = nxt.start()
    return text[start:min(cut, end)].strip()


def extract_sections(text: str) -> dict[str, str]:
    """Pull intro / method / limitations slices from extracted PDF text.

    Falls back to a head-and-tail slice when no headings are detected
    (some PDFs have funny layouts that pypdf can't recover headings from)."""
    body = _strip_after_refs(text)
    intro = _slice_section(body, _RE_INTRO, INTRO_CHARS)
    method = _slice_section(body, _RE_METHOD, METHOD_CHARS)
    limits = _slice_section(body, _RE_LIMITS, LIMITS_CHARS)
    if not (intro or method or limits):
        # Heading-free fallback: front loads tend to carry intro/motivation,
        # tail tends to carry limitations / conclusion.
        return {
            "fallback_head": body[:FALLBACK_HEAD].strip(),
            "fallback_tail": body[-FALLBACK_TAIL:].strip(),
        }
    return {"intro": intro, "method": method, "limitations": limits}


def extract_text(pdf_bytes: bytes) -> str:
    """pypdf text extract; raises on malformed PDFs."""
    from pypdf import PdfReader  # imported lazily so pure-meta paths don't pay
    reader = PdfReader(io.BytesIO(pdf_bytes))
    parts: list[str] = []
    for page in reader.pages:
        try:
            parts.append(page.extract_text() or "")
        except Exception:  # noqa: BLE001 — page-level extraction can fault
            continue
    text = "\n".join(parts)
    # Common pypdf artifact: split-word ligatures / stray dashes on line wraps.
    text = re.sub(r"-\n([a-z])", r"\1", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def fetch_pdf(paper: "Paper") -> bytes | None:
    """Best-effort PDF download. Returns None on any failure (logged once
    so the caller can show a summary, but the run continues)."""
    url = paper.pdf_url
    if not url:
        return None
    try:
        r = requests.get(url, headers={"User-Agent": USER_AGENT},
                         timeout=PDF_TIMEOUT_SECONDS, stream=True)
        if r.status_code != 200:
            return None
        # Stream-with-cap so a runaway response can't OOM us.
        chunks: list[bytes] = []
        size = 0
        for chunk in r.iter_content(chunk_size=64 * 1024):
            if not chunk:
                continue
            size += len(chunk)
            if size > PDF_MAX_BYTES:
                return None
            chunks.append(chunk)
        return b"".join(chunks)
    except Exception:  # noqa: BLE001 — network is unreliable; fall through
        return None


def get_or_fetch(paper: "Paper", cache_dir: Path,
                 *, ensure_raw_pdf: bool = False) -> dict | None:
    """Return cached entry {sections, fetched_at, source} or fetch+cache.
    None if fetch failed or PDF was unparseable.

    Sections (JSON) and raw bytes (PDF) are cached side-by-side in cache_dir
    keyed by `_cache_key(paper.get_id())`. With ``ensure_raw_pdf=True`` we
    *lazily upgrade* old cache entries that only have sections (pre-archive
    feature) by refetching the PDF, so downstream archive-to-report can
    hardlink the bytes."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    pid = paper.get_id()
    jpath = _cache_path(pid, cache_dir)
    pdf_path = _pdf_path(pid, cache_dir)
    if jpath.exists():
        try:
            entry = json.loads(jpath.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001 — corrupted cache; refetch below
            jpath.unlink(missing_ok=True)
            entry = None
        if entry is not None:
            if ensure_raw_pdf and not pdf_path.exists():
                raw = fetch_pdf(paper)
                if raw:
                    pdf_path.write_bytes(raw)
            return entry
    pdf = fetch_pdf(paper)
    if pdf is None:
        return None
    pdf_path.write_bytes(pdf)
    try:
        text = extract_text(pdf)
    except Exception:  # noqa: BLE001 — malformed PDF; drop bytes, return None
        pdf_path.unlink(missing_ok=True)
        return None
    if not text:
        pdf_path.unlink(missing_ok=True)
        return None
    entry = {
        "id": pid,
        "title": paper.title,
        "sections": extract_sections(text),
        "fetched_at": int(time.time()),
        "source": paper.pdf_url,
    }
    jpath.write_text(json.dumps(entry, ensure_ascii=False), encoding="utf-8")
    return entry


def build_deep_context(papers: list["Paper"], *, k: int = 10,
                       cache_dir: Path = CACHE_DIR_DEFAULT,
                       ensure_raw_pdf: bool = True) -> tuple[str, dict]:
    """Build the markdown deep_context block fed to Skeptic + Proposer.

    Returns (text, stats) where stats has counts of fetched/cached/failed
    so the caller can surface a one-line summary in CLI output and report
    metadata. ``ensure_raw_pdf=True`` (the default once archive-to-report
    landed) means cache entries missing raw bytes are lazily upgraded so
    the archive step has something to hardlink."""
    from skills.topic_finder.scripts.build_report import _short_id  # re-use id rendering
    out: list[str] = ["## Deep PDF context (top-{k} matched papers, sectioned)\n".format(k=k)]
    stats = {"requested": min(k, len(papers)), "ok": 0, "cached_hit": 0,
             "fetched": 0, "failed": 0}
    for p in papers[:k]:
        cpath = _cache_path(p.get_id(), cache_dir)
        was_cached = cpath.exists()
        entry = get_or_fetch(p, cache_dir, ensure_raw_pdf=ensure_raw_pdf)
        if entry is None:
            stats["failed"] += 1
            continue
        stats["ok"] += 1
        if was_cached:
            stats["cached_hit"] += 1
        else:
            stats["fetched"] += 1
        sid = _short_id(p.get_id(), p.venue)
        out.append(f"### [{sid}] {p.title}")
        secs = entry.get("sections") or {}
        for label in ("intro", "method", "limitations",
                      "fallback_head", "fallback_tail"):
            txt = (secs.get(label) or "").strip()
            if not txt:
                continue
            out.append(f"**{label}:**")
            out.append(txt)
        out.append("")
    return "\n".join(out), stats


def archive_to_report(papers: list["Paper"], *, cache_dir: Path,
                      archive_dir: Path) -> dict:
    """Hardlink raw PDFs from cache_dir into archive_dir/<short-id>.pdf
    and write archive_dir/manifest.json describing what's there.

    Hardlinks need same filesystem; we fall back to ``shutil.copy2`` on
    cross-FS (EXDEV) so the archive still works on weird mounts. Skip
    silently when a paper has no raw bytes in cache (e.g. a fetch attempt
    that hit a 4xx); the manifest records it as ``raw_pdf: missing``."""
    import os
    import shutil

    from skills.topic_finder.scripts.build_report import _short_id

    archive_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[dict] = []
    stats = {"linked": 0, "copied": 0, "missing": 0}
    for p in papers:
        pid = p.get_id()
        src = _pdf_path(pid, cache_dir)
        sid = _short_id(pid, p.venue)
        entry: dict = {
            "id": pid, "short_id": sid, "title": p.title,
            "venue": p.venue, "date": (p.published_date.isoformat()
                                       if p.published_date else None),
            "source_url": p.pdf_url,
        }
        if not src.exists():
            entry["raw_pdf"] = "missing"
            stats["missing"] += 1
            manifest.append(entry)
            continue
        dst = archive_dir / f"{sid}.pdf"
        if dst.exists():
            entry["raw_pdf"] = dst.name
            entry["linked"] = "already_present"
            manifest.append(entry)
            continue
        try:
            os.link(src, dst)  # hardlink — same-FS, no extra disk
            stats["linked"] += 1
            entry["linked"] = "hardlink"
        except OSError:  # cross-FS or permission — fall back to copy
            shutil.copy2(src, dst)
            stats["copied"] += 1
            entry["linked"] = "copy"
        entry["raw_pdf"] = dst.name
        manifest.append(entry)
    (archive_dir / "manifest.json").write_text(
        json.dumps({"papers": manifest, "stats": stats},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return stats


if __name__ == "__main__":
    # Tiny CLI for ad-hoc inspection: extract one paper id from the rolling DB.
    import argparse
    import sys
    REPO_ROOT = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(REPO_ROOT))
    from skills.topic_finder.scripts.load_metadb import load_rolling

    ap = argparse.ArgumentParser()
    ap.add_argument("paper_id", help="e.g. arxiv:2604.21251")
    ap.add_argument("--cache-dir", default="metadb/.pdfs")
    args = ap.parse_args()

    target_id = args.paper_id
    papers = load_rolling()
    p = next((x for x in papers if x.get_id() == target_id), None)
    if not p:
        sys.exit(f"paper not found in rolling DB: {target_id}")
    entry = get_or_fetch(p, Path(args.cache_dir))
    if entry is None:
        sys.exit("fetch / extract failed")
    print(json.dumps(entry, ensure_ascii=False, indent=2))
