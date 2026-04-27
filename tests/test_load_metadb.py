import json
from datetime import date
from pathlib import Path

from collector.src.models import Paper
from skills.topic_finder.scripts.load_metadb import load_rolling


def _write_month(root: Path, ym: str, papers: list[Paper]) -> None:
    target = root / f"{ym}_rolling.jsonl"
    target.write_text(
        "\n".join(json.dumps(p.to_jsonl_dict()) for p in papers) + "\n",
        encoding="utf-8",
    )


def test_load_rolling_returns_paper_objects(tmp_path: Path):
    p = Paper(title="Test", arxiv_id="2404.0001",
              published_date=date(2026, 4, 26), source="arxiv")
    _write_month(tmp_path, "2604", [p])

    loaded = load_rolling(tmp_path)
    assert len(loaded) == 1
    assert loaded[0].arxiv_id == "2404.0001"


def test_load_rolling_returns_empty_when_dir_missing(tmp_path: Path):
    assert load_rolling(tmp_path / "missing") == []


def test_load_rolling_concatenates_month_files(tmp_path: Path):
    apr = Paper(title="A", arxiv_id="2404.0001",
                published_date=date(2026, 4, 10), source="arxiv")
    mar = Paper(title="M", arxiv_id="2403.0001",
                published_date=date(2026, 3, 5), source="arxiv")
    _write_month(tmp_path, "2604", [apr])
    _write_month(tmp_path, "2603", [mar])

    loaded = load_rolling(tmp_path)
    assert {p.arxiv_id for p in loaded} == {"2404.0001", "2403.0001"}


def test_load_rolling_respects_since_filter(tmp_path: Path):
    apr = Paper(title="A", arxiv_id="2404.0001",
                published_date=date(2026, 4, 10), source="arxiv")
    mar = Paper(title="M", arxiv_id="2403.0001",
                published_date=date(2026, 3, 5), source="arxiv")
    _write_month(tmp_path, "2604", [apr])
    _write_month(tmp_path, "2603", [mar])

    loaded = load_rolling(tmp_path, since=date(2026, 4, 1))
    assert {p.arxiv_id for p in loaded} == {"2404.0001"}
