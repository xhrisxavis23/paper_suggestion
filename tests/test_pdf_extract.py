"""Unit tests for skills.topic_finder.scripts.pdf_extract — section extraction
heuristics. We don't exercise the network/PDF path here; that's covered by the
integration suite (`pytest -m integration`). These tests pin the regex behavior
that decides what Skeptic / Proposer see under --deep."""

import textwrap
from pathlib import Path

import pytest

from skills.topic_finder.scripts.pdf_extract import (
    _strip_after_refs,
    extract_sections,
)


def _arxiv_like(intro: str, method: str, limits: str = "") -> str:
    """Build a synthetic paper body that looks like arxiv-LaTeX output."""
    body = f"""
    Title: Some Paper

    Abstract
    Lorem ipsum dolor sit amet.

    1. Introduction
    {intro}

    2. Related Work
    Prior work A. Prior work B.

    3. Method
    {method}

    4. Experiments
    We tested on dataset Z.

    5. Limitations
    {limits or 'None reported.'}

    References
    [1] Goodfellow et al.
    """
    return textwrap.dedent(body)


def test_extract_sections_basic_arxiv_layout():
    txt = _arxiv_like(
        intro="This paper proposes Foo to solve Bar.",
        method="We use a transformer with trick T.",
        limits="Our approach fails when X happens.",
    )
    secs = extract_sections(txt)
    assert "intro" in secs and "method" in secs and "limitations" in secs
    assert "Foo" in secs["intro"]
    assert "trick T" in secs["method"]
    assert "fails when X" in secs["limitations"]


def test_extract_sections_does_not_match_prose_approach():
    """Regression: prose like 'Our approach fails when X.' must NOT register
    as a Method heading and prematurely cut the previous section."""
    txt = _arxiv_like(
        intro="Intro line.",
        method="We use Y.",
        limits="Our approach fails when X happens.",
    )
    secs = extract_sections(txt)
    # The 'fails when X' phrase belongs in limitations, not chopped off.
    assert "fails when X" in secs["limitations"]


def test_extract_sections_strips_references():
    txt = _arxiv_like(
        intro="Intro.", method="Method.", limits="Lim.",
    )
    body = _strip_after_refs(txt)
    assert "Goodfellow" not in body
    secs = extract_sections(txt)
    # No section should include the references list.
    for s in secs.values():
        assert "Goodfellow" not in s


def test_extract_sections_falls_back_when_no_headings():
    """Some PDFs lose section markers via pypdf — fall back to head+tail
    so Skeptic / Proposer still see *something* useful."""
    raw = (
        "Some abstract-like opening "
        "describing the contribution of the paper. "
        + ("Some filler. " * 200)
        + "Final remark before bibliography."
    )
    secs = extract_sections(raw)
    assert "fallback_head" in secs
    assert "fallback_tail" in secs
    assert "abstract-like opening" in secs["fallback_head"]
    assert "Final remark" in secs["fallback_tail"]


def test_extract_sections_handles_uppercase_headings():
    raw = textwrap.dedent("""
    INTRODUCTION
    The motivation for this work.

    METHOD
    Step-by-step procedure.

    LIMITATIONS
    Known caveats.

    REFERENCES
    [1] X.
    """)
    secs = extract_sections(raw)
    assert "motivation" in secs.get("intro", "")
    assert "procedure" in secs.get("method", "")
    assert "Known caveats" in secs.get("limitations", "")


def test_extract_sections_truncates_long_section_to_budget():
    """Method budget is INTRO_CHARS / METHOD_CHARS / LIMITS_CHARS = 1500.
    A 5000-char method section should be cut around 1500."""
    long_method = "We use a transformer. " * 500  # ≈10K chars
    raw = _arxiv_like(intro="I.", method=long_method, limits="L.")
    secs = extract_sections(raw)
    assert 200 < len(secs["method"]) <= 1600  # 1500 budget + small slack
