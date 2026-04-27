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
    db = RollingDB(tmp_path)
    p1 = make_paper("2404.0001", date(2026, 4, 26))
    p2 = make_paper("2404.0002", date(2026, 4, 25))

    added = db.append([p1, p2])
    assert len(added) == 2

    loaded = db.load_all()
    ids = {p.get_id() for p in loaded}
    assert ids == {"arxiv:2404.0001", "arxiv:2404.0002"}


def test_append_dedupes_by_id(tmp_path: Path):
    db = RollingDB(tmp_path)
    p = make_paper("2404.0001", date(2026, 4, 26))

    assert len(db.append([p])) == 1
    assert db.append([p]) == []  # second time: no new entries

    loaded = db.load_all()
    assert len(loaded) == 1


def test_append_dedupes_in_batch_and_preserves_order(tmp_path: Path):
    db = RollingDB(tmp_path)
    p1 = make_paper("2404.0001", date(2026, 4, 26))
    p2 = make_paper("2404.0002", date(2026, 4, 25))
    p1_dup = make_paper("2404.0001", date(2026, 4, 26))

    added = db.append([p1, p2, p1_dup, p2])
    assert [p.arxiv_id for p in added] == ["2404.0001", "2404.0002"]
    assert len(db.load_all()) == 2


def test_append_partitions_by_month(tmp_path: Path):
    db = RollingDB(tmp_path)
    p_apr = make_paper("2404.0001", date(2026, 4, 26))
    p_mar = make_paper("2403.0001", date(2026, 3, 15))

    db.append([p_apr, p_mar])

    assert (tmp_path / "2604_rolling.jsonl").exists()
    assert (tmp_path / "2603_rolling.jsonl").exists()
    # April file holds only April paper
    apr_lines = (tmp_path / "2604_rolling.jsonl").read_text().splitlines()
    assert len(apr_lines) == 1
    assert "2404.0001" in apr_lines[0]


def test_prune_drops_whole_old_month_files(tmp_path: Path):
    db = RollingDB(tmp_path)
    today = date(2026, 4, 26)
    fresh = make_paper("2404.0001", today - timedelta(days=10))   # 2026-04-16
    stale = make_paper("2402.0001", date(2026, 2, 1))             # 2602 month

    db.append([fresh, stale])
    pruned = db.prune(today=today, window_days=30)  # cutoff 2026-03-27

    # 2602 file (whole month before cutoff) gone; 2604 untouched.
    assert pruned == 1
    assert not (tmp_path / "2602_rolling.jsonl").exists()
    assert (tmp_path / "2604_rolling.jsonl").exists()
    remaining_ids = {p.get_id() for p in db.load_all()}
    assert remaining_ids == {"arxiv:2404.0001"}


def test_prune_filters_within_cutoff_month(tmp_path: Path):
    db = RollingDB(tmp_path)
    today = date(2026, 4, 26)                                    # cutoff = 04-12
    keep = make_paper("2404.0001", date(2026, 4, 20))            # after cutoff
    drop_early = make_paper("2404.0002", date(2026, 4, 1))       # before cutoff
    keep_at_cutoff = make_paper("2404.0003", date(2026, 4, 12))  # == cutoff (kept)

    db.append([keep, drop_early, keep_at_cutoff])
    pruned = db.prune(today=today, window_days=14)

    assert pruned == 1
    remaining = {p.get_id() for p in db.load_all()}
    assert remaining == {"arxiv:2404.0001", "arxiv:2404.0003"}


def test_load_all_on_missing_dir_returns_empty(tmp_path: Path):
    db = RollingDB(tmp_path / "nope")
    assert db.load_all() == []


def test_append_skips_papers_with_no_published_date(tmp_path: Path):
    db = RollingDB(tmp_path)
    p_dated = make_paper("2404.0001", date(2026, 4, 26))
    p_nodate = Paper(title="undated", arxiv_id="2404.9999",
                     published_date=None, source="hf")

    added = db.append([p_dated, p_nodate])
    assert len(added) == 1
    assert added[0].arxiv_id == "2404.0001"
