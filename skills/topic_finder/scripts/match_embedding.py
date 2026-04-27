"""Embedding-based matching of a topic against the rolling DB (M-2, opt-in).

Heavyweight deps — install separately:
    pip install -r collector/requirements-embedding.txt

Index is cached at <root>/metadb/.embeddings/ (gitignored). Rebuilt when the
set of paper ids in the DB changes (e.g., after a fresh collector run).

CLI:
    python -m skills.topic_finder.scripts.match_embedding \\
        --topic "sparse autoencoder" \\
        --out reports/.cache/<run>/matched.jsonl \\
        --window-days 60 --top-k 200
"""
from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import List

_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from collector.src.models import Paper
from skills.topic_finder.scripts.load_metadb import DEFAULT_ROLLING_DIR, load_rolling

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_CACHE_DIR_NAME = ".embeddings"


def _import_deps():
    try:
        import faiss  # type: ignore
        from sentence_transformers import SentenceTransformer  # type: ignore
    except ImportError as e:
        raise SystemExit(
            f"embedding mode requires sentence-transformers + faiss-cpu: "
            f"`pip install -r collector/requirements-embedding.txt` ({e})"
        )
    return faiss, SentenceTransformer


def _paper_text(p: Paper) -> str:
    return (p.title + ". " + (p.abstract or ""))[:2000]


def build_or_load_index(papers: List[Paper], cache_dir: Path):
    faiss, SentenceTransformer = _import_deps()
    cache_dir.mkdir(parents=True, exist_ok=True)
    idx_path = cache_dir / "index.faiss"
    ids_path = cache_dir / "ids.json"
    cur_ids = [p.get_id() for p in papers]

    if idx_path.exists() and ids_path.exists():
        cached_ids = json.loads(ids_path.read_text())
        if cached_ids == cur_ids:
            return faiss.read_index(str(idx_path)), cached_ids

    print(f"[embedding] building index over {len(papers)} papers…", flush=True)
    model = SentenceTransformer(EMBEDDING_MODEL)
    embs = model.encode(
        [_paper_text(p) for p in papers],
        batch_size=64, show_progress_bar=True, convert_to_numpy=True,
    )
    dim = embs.shape[1]
    index = faiss.IndexFlatIP(dim)
    faiss.normalize_L2(embs)
    index.add(embs)
    faiss.write_index(index, str(idx_path))
    ids_path.write_text(json.dumps(cur_ids))
    print(f"[embedding] index cached at {idx_path}", flush=True)
    return index, cur_ids


def search_embedding(papers: List[Paper], topic: str, top_k: int) -> List[Paper]:
    faiss, SentenceTransformer = _import_deps()
    cache_dir = _REPO_ROOT / "metadb" / EMBEDDING_CACHE_DIR_NAME
    index, ids = build_or_load_index(papers, cache_dir)
    model = SentenceTransformer(EMBEDDING_MODEL)
    q = model.encode([topic], convert_to_numpy=True)
    faiss.normalize_L2(q)
    scores, idxs = index.search(q, top_k)
    by_id = {p.get_id(): p for p in papers}
    out: List[Paper] = []
    for i in idxs[0]:
        if 0 <= i < len(ids) and ids[i] in by_id:
            out.append(by_id[ids[i]])
    return out


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--rolling-dir", default=str(DEFAULT_ROLLING_DIR))
    parser.add_argument("--topic", required=True,
                        help="Free-form topic string (encoded into the query).")
    parser.add_argument("--out", required=True)
    parser.add_argument("--window-days", type=int, default=None)
    parser.add_argument("--top-k", type=int, default=200)
    args = parser.parse_args()

    since = (
        date.today() - timedelta(days=args.window_days)
        if args.window_days is not None else None
    )
    papers = load_rolling(Path(args.rolling_dir), since=since)
    matched = search_embedding(papers, args.topic, args.top_k)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for p in matched:
            f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")
    print(f"[embedding] top-{args.top_k} → {args.out}")
