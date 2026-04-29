"""Import a manually-downloaded PDF into the deep-mode cache.

For paywalled venues (e.g., IEEE TII, Elsevier ESWA) `/find-topic --deep`
cannot fetch the PDF itself — `paper.pdf_url` is empty or points at a DOI
gateway returning HTML. Once you have a legitimate copy (e.g., via
institutional access), this script drops it into `metadb/.pdfs/` in the
format `pdf_extract.get_or_fetch` expects, so the next `--deep` run picks
it up via cache hit instead of re-attempting the failing fetch.

Usage (most common — pick the paper out of a report's manifest by short id):

    python -m skills.topic_finder.scripts.import_pdf \\
        --pdf ~/Downloads/coma-ikg.pdf \\
        --manifest reports/2026-04-28-manufacturing-multi-agent-gemini-pro-deep/manifest.json \\
        --short-id IEEETRAN-bf3127

Batch mode — drop every paywall PDF into `metadb/pdf_inbox/<short-id>.pdf`
(filename stem must equal a `short_id` from the manifest), then:

    python -m skills.topic_finder.scripts.import_pdf \\
        --manifest reports/<stem>/manifest.json --inbox

Successfully imported files are moved to `metadb/pdf_inbox/.imported/`.

Manual mode (when you already know the paper id):

    python -m skills.topic_finder.scripts.import_pdf \\
        --pdf ~/Downloads/coma-ikg.pdf \\
        --paper-id "title:coma-ikg llm-driven multiagent framework..." \\
        --title "CoMA-IKG: LLM-Driven Multiagent Framework ..."
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from skills.topic_finder.scripts.pdf_extract import (
    CACHE_DIR_DEFAULT,
    _cache_path,
    _pdf_path,
    extract_sections,
    extract_text,
)


def _resolve_from_manifest(
    manifest_path: Path, short_id: str
) -> tuple[str, str, str | None]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    papers = data.get("papers", [])
    # Accept both "P-<sid>" and bare "<sid>" — manifest stores bare.
    needle = short_id[2:] if short_id.startswith("P-") else short_id
    exact = [p for p in papers if p.get("short_id") == needle]
    if exact:
        matches = exact
    else:
        # Suffix match so the user can paste a partial hash (e.g. "a3f29d").
        matches = [p for p in papers if p.get("short_id", "").endswith(needle)]
    if not matches:
        sys.exit(f"short-id not found in manifest: {short_id}")
    if len(matches) > 1:
        names = ", ".join(p["short_id"] for p in matches)
        sys.exit(f"short-id ambiguous ({len(matches)} matches): {names}")
    p = matches[0]
    return p["id"], p["title"], p.get("source_url")


INBOX_DIR_DEFAULT = Path("metadb/pdf_inbox")


def _import_one(
    pdf_path: Path, paper_id: str, title: str,
    source: str | None, cache_dir: Path,
) -> dict:
    """Copy bytes + write extracted-sections JSON. Returns sections dict.
    Raises SystemExit on unrecoverable failure (bad PDF, no text)."""
    pdf_bytes = pdf_path.read_bytes()
    if not pdf_bytes.startswith(b"%PDF"):
        sys.exit(
            f"file does not look like a PDF (no %PDF header): {pdf_path}"
        )
    try:
        text = extract_text(pdf_bytes)
    except Exception as e:  # noqa: BLE001 — pypdf raises a zoo of exception types
        sys.exit(f"pypdf could not parse {pdf_path.name}: {e}")
    if not text.strip():
        sys.exit(
            f"pypdf extracted no text from {pdf_path.name} — "
            "image-only / scanned / encrypted PDF?"
        )

    cache_dir.mkdir(parents=True, exist_ok=True)
    dst_pdf = _pdf_path(paper_id, cache_dir)
    dst_json = _cache_path(paper_id, cache_dir)
    shutil.copy2(pdf_path, dst_pdf)
    entry = {
        "id": paper_id,
        "title": title,
        "sections": extract_sections(text),
        "fetched_at": int(time.time()),
        "source": source or f"manual-import:{pdf_path.name}",
    }
    dst_json.write_text(
        json.dumps(entry, ensure_ascii=False), encoding="utf-8"
    )
    return entry


def _run_inbox(manifest: Path, inbox: Path, cache_dir: Path) -> None:
    """Walk `inbox` for *.pdf, match each by stem to a manifest short_id,
    import, then move successful files to inbox/.imported/.

    Special case: if `inbox` is the same folder as the manifest (i.e. the
    report bundle directory), imported PDFs are *kept in place* — they
    belong there as part of the report archive and would be confusing to
    move into `.imported/`. Already-cached papers are skipped silently so
    re-runs are safe."""
    if not inbox.exists():
        sys.exit(f"inbox not found: {inbox}")
    pdfs = sorted(p for p in inbox.glob("*.pdf"))
    if not pdfs:
        sys.exit(f"no *.pdf files in {inbox}")

    same_as_report = inbox.resolve() == manifest.parent.resolve()
    archive = None if same_as_report else inbox / ".imported"
    if archive is not None:
        archive.mkdir(exist_ok=True)

    ok, skipped, fail = 0, 0, 0
    for pdf in pdfs:
        try:
            paper_id, title, source = _resolve_from_manifest(manifest, pdf.stem)
        except SystemExit as e:
            print(f"  skip {pdf.name}: {e}")
            fail += 1
            continue
        if _cache_path(paper_id, cache_dir).exists():
            print(f"  cached {pdf.name} -> {paper_id} (already imported)")
            skipped += 1
            continue
        entry = _import_one(pdf, paper_id, title, source, cache_dir)
        secs = entry["sections"]
        summary = ", ".join(f"{k}={len(v)}c" for k, v in secs.items() if v)
        print(f"  imported {pdf.name} -> {paper_id}  [{summary or '(empty)'}]")
        if archive is not None:
            shutil.move(str(pdf), str(archive / pdf.name))
        ok += 1

    tail = (f"Archived to {archive}/" if archive is not None
            else "(kept in place — report bundle directory)")
    print(f"\nDone: {ok} imported, {skipped} cached, {fail} skipped. {tail}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Import a manually-downloaded PDF into the deep cache."
    )
    ap.add_argument("--pdf", help="Path to a single PDF (single-file mode).")
    ap.add_argument(
        "--inbox-dir", default=str(INBOX_DIR_DEFAULT),
        help=f"Inbox folder for batch mode (default: {INBOX_DIR_DEFAULT}).",
    )
    ap.add_argument(
        "--inbox", action="store_true",
        help="Batch mode: import every *.pdf in --inbox-dir whose stem "
             "matches a short_id in --manifest.",
    )
    ap.add_argument(
        "--manifest",
        help="reports/<stem>/manifest.json — pulls id+title from short-id.",
    )
    ap.add_argument(
        "--short-id",
        help="short_id from manifest (with or without 'P-' prefix; "
             "trailing-suffix match also accepted).",
    )
    ap.add_argument(
        "--paper-id",
        help="Manual paper id (e.g. 'title:...'). Use when no manifest.",
    )
    ap.add_argument(
        "--title",
        help="Paper title (required with --paper-id).",
    )
    ap.add_argument("--cache-dir", default=str(CACHE_DIR_DEFAULT))
    args = ap.parse_args()

    cache_dir = Path(args.cache_dir)

    if args.inbox:
        if not args.manifest:
            sys.exit("--inbox requires --manifest")
        _run_inbox(Path(args.manifest), Path(args.inbox_dir), cache_dir)
        return

    if not args.pdf:
        sys.exit(
            "Provide either --pdf <path> (single-file) or --inbox (batch)."
        )

    pdf_path = Path(args.pdf).expanduser()
    if not pdf_path.exists():
        sys.exit(f"PDF not found: {pdf_path}")

    if args.manifest:
        if not args.short_id:
            sys.exit("--manifest requires --short-id (or use --inbox)")
        paper_id, title, source = _resolve_from_manifest(
            Path(args.manifest), args.short_id
        )
    else:
        if not args.paper_id or not args.title:
            sys.exit(
                "Either --manifest+--short-id or --paper-id+--title is required."
            )
        paper_id, title, source = args.paper_id, args.title, None

    entry = _import_one(pdf_path, paper_id, title, source, cache_dir)
    secs = entry["sections"]
    sec_summary = ", ".join(
        f"{k}={len(v)}c" for k, v in secs.items() if v
    )
    print(f"Imported: {paper_id}")
    print(f"  PDF  -> {_pdf_path(paper_id, cache_dir)}")
    print(f"  JSON -> {_cache_path(paper_id, cache_dir)}")
    print(f"  sections: {sec_summary or '(none extracted; check PDF layout)'}")


if __name__ == "__main__":
    main()
