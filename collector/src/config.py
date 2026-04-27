"""Collector configuration: categories, venues, no topic filter."""
from __future__ import annotations

# arXiv categories to collect (no topic filter)
ARXIV_CATEGORIES = [
    "cs.AI",
    "cs.LG",
    "cs.CL",
    "cs.CV",
    "cs.RO",
    "stat.ML",
]

# How many days of arXiv submissions to query each run
ARXIV_LOOKBACK_DAYS = 1

# Max arXiv results per category per run (API hard cap is 2000; safety buffer)
ARXIV_MAX_RESULTS_PER_CATEGORY = 500

# Conferences to query via Semantic Scholar (last 30 days of published papers)
S2_VENUES = ["AAAI", "NeurIPS", "ICML", "ICLR", "CVPR", "KDD"]

# OpenReview venue ids (active venues)
OPENREVIEW_VENUE_IDS = [
    "ICLR.cc/2026/Conference",
    # Add NeurIPS / ICML when active
]

# HuggingFace daily papers fallback window
HF_FALLBACK_DAYS = 3

# User-Agent for requests
USER_AGENT = "paper-suggestion-bot/0.1"

# Rolling window in days
ROLLING_WINDOW_DAYS = 60

# Default paths (relative to repo root)
METADB_DIR = "metadb"
# Rolling DB is partitioned by month under ROLLING_DIR — files named
# <YYMM>_rolling.jsonl (e.g. 2604_rolling.jsonl). See collector.src.db.RollingDB.
ROLLING_DIR = "metadb"
DAILY_DIR = "metadb/daily"
STATS_JSON = "metadb/stats.json"
STATS_HISTORY_JSONL = "metadb/stats_history.jsonl"
