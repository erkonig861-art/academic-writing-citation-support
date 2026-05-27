#!/usr/bin/env python3
"""Heuristic APA in-text/reference cross-check for plain text drafts.

The script catches likely orphan citations and uncited references. It is not a
complete APA parser; manually review complex citations.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


YEAR_RE = r"(?:19|20)\d{2}[a-z]?"
STOPWORDS = {
    "see",
    "e.g.",
    "cf.",
    "and",
    "as",
    "cited",
    "in",
}


def normalize_author(text: str) -> str:
    text = re.sub(r"\bet al\.?", "", text, flags=re.I)
    text = re.sub(r"\[[^\]]+\]", "", text)
    text = text.replace("&", " and ")
    text = re.split(r"\band\b|,", text)[0]
    text = re.sub(r"[^A-Za-zÀ-ÖØ-öø-ÿ'\- ]", " ", text)
    parts = [p for p in text.split() if p.lower() not in STOPWORDS]
    return (parts[-1] if parts else "").lower()


def split_references(text: str) -> tuple[str, str]:
    match = re.search(r"(?im)^\s*(references|reference list|bibliography)\s*$", text)
    if not match:
        return text, ""
    return text[: match.start()], text[match.end() :]


def extract_intext(body: str) -> set[tuple[str, str]]:
    found: set[tuple[str, str]] = set()

    # Parenthetical citations: (Smith, 2020; Jones & Lee, 2021)
    for group in re.findall(r"\(([^()]*?" + YEAR_RE + r"[^()]*)\)", body):
        for part in group.split(";"):
            years = re.findall(YEAR_RE, part)
            if not years:
                continue
            author = normalize_author(part.split(years[0])[0])
            if author:
                found.add((author, years[0]))

    # Narrative citations: Smith (2020), Smith and Lee (2020)
    narrative_re = re.compile(
        r"\b([A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+(?:\s+(?:and|&)\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'\-]+)?(?:\s+et al\.?)?)\s*\(("
        + YEAR_RE
        + r")\)"
    )
    for author_text, year in narrative_re.findall(body):
        author = normalize_author(author_text)
        if author:
            found.add((author, year))

    return found


def extract_refs(refs: str) -> set[tuple[str, str]]:
    found: set[tuple[str, str]] = set()
    entries = re.split(r"\n\s*\n|\n(?=[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÖØ-öø-ÿ'\-]+,\s+[A-Z])", refs)
    for entry in entries:
        entry = " ".join(entry.split())
        if not entry:
            continue
        year_match = re.search(r"\((" + YEAR_RE + r")\)", entry)
        if not year_match:
            continue
        first_part = entry[: year_match.start()]
        author = normalize_author(first_part)
        if author:
            found.add((author, year_match.group(1)))
    return found


def fmt(items: set[tuple[str, str]]) -> str:
    return ", ".join(f"{author.title()} ({year})" for author, year in sorted(items)) or "None"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Plain text or Markdown file containing body and references")
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    body, refs = split_references(text)
    intext = extract_intext(body)
    ref_entries = extract_refs(refs)

    missing_refs = intext - ref_entries
    uncited_refs = ref_entries - intext

    print("# APA Citation Cross-Check")
    print(f"In-text citation keys: {len(intext)}")
    print(f"Reference-list keys: {len(ref_entries)}")
    print(f"Likely in-text citations missing from references: {len(missing_refs)}")
    print(fmt(missing_refs))
    print(f"Likely reference entries not cited in text: {len(uncited_refs)}")
    print(fmt(uncited_refs))

    return 1 if missing_refs or uncited_refs else 0


if __name__ == "__main__":
    raise SystemExit(main())
