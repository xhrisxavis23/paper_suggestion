from datetime import date
from pathlib import Path

from collector.src.models import Paper
from skills.topic_finder.scripts.load_metadb import load_rolling


def test_load_rolling_returns_paper_objects(tmp_path: Path):
    p = Paper(title="Test", arxiv_id="2404.0001",
              published_date=date(2026, 4, 26), source="arxiv")
    target = tmp_path / "rolling.jsonl"
    target.write_text(__import__("json").dumps(p.to_jsonl_dict()) + "\n",
                      encoding="utf-8")

    loaded = load_rolling(target)
    assert len(loaded) == 1
    assert loaded[0].arxiv_id == "2404.0001"


def test_load_rolling_returns_empty_when_missing(tmp_path: Path):
    assert load_rolling(tmp_path / "missing.jsonl") == []
