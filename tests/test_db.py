from datetime import date, timedelta
from pathlib import Path

import pytest

from collector.src.models import Paper
from collector.src.db import RollingDB


def make_paper(arxiv_id: str, d: date) -> Paper:
    return Paper(
        title=f"Title {arxiv_id}",
        abstract="abs",
        authors=["Alice"],
        arxiv_id=arxiv_id,
        published_date=d,
        source="arxiv",
    )


def test_append_then_load(tmp_path: Path):
    db = RollingDB(tmp_path / "rolling.jsonl")
    p1 = make_paper("2404.0001", date(2026, 4, 26))
    p2 = make_paper("2404.0002", date(2026, 4, 25))

    added = db.append([p1, p2])
    assert len(added) == 2

    loaded = db.load_all()
    ids = {p.get_id() for p in loaded}
    assert ids == {"arxiv:2404.0001", "arxiv:2404.0002"}


def test_append_dedupes_by_id(tmp_path: Path):
    db = RollingDB(tmp_path / "rolling.jsonl")
    p = make_paper("2404.0001", date(2026, 4, 26))

    assert len(db.append([p])) == 1
    assert db.append([p]) == []  # second time: no new entries

    loaded = db.load_all()
    assert len(loaded) == 1


def test_append_dedupes_in_batch_and_preserves_order(tmp_path: Path):
    db = RollingDB(tmp_path / "rolling.jsonl")
    p1 = make_paper("2404.0001", date(2026, 4, 26))
    p2 = make_paper("2404.0002", date(2026, 4, 25))
    p1_dup = make_paper("2404.0001", date(2026, 4, 26))

    added = db.append([p1, p2, p1_dup, p2])
    assert [p.arxiv_id for p in added] == ["2404.0001", "2404.0002"]
    assert len(db.load_all()) == 2


def test_prune_drops_old_entries(tmp_path: Path):
    db = RollingDB(tmp_path / "rolling.jsonl")
    today = date(2026, 4, 26)
    fresh = make_paper("2404.0001", today - timedelta(days=10))
    stale = make_paper("2403.0001", today - timedelta(days=40))

    db.append([fresh, stale])
    pruned = db.prune(today=today, window_days=30)

    assert pruned == 1
    remaining_ids = {p.get_id() for p in db.load_all()}
    assert remaining_ids == {"arxiv:2404.0001"}


def test_load_all_on_missing_file_returns_empty(tmp_path: Path):
    db = RollingDB(tmp_path / "nope.jsonl")
    assert db.load_all() == []
