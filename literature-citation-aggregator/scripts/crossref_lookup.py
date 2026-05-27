#!/usr/bin/env python3
"""Lookup Crossref metadata by DOI or title and print APA-like drafts.

This is a helper for verification, not a replacement for relevance review.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "literature-citation-aggregator/1.0 (mailto:example@example.com)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def year_from(item: dict) -> str:
    for key in ("published-print", "published-online", "issued"):
        parts = item.get(key, {}).get("date-parts")
        if parts and parts[0]:
            return str(parts[0][0])
    return "n.d."


def author_name(author: dict) -> str:
    family = author.get("family", "").strip()
    given = author.get("given", "").strip()
    if not family:
        return given or "Unknown"
    initials = " ".join(part[0] + "." for part in given.replace("-", " ").split() if part)
    return f"{family}, {initials}" if initials else family


def authors_apa(authors: list[dict]) -> str:
    names = [author_name(a) for a in authors if isinstance(a, dict)]
    if not names:
        return "Unknown author"
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]}, & {names[1]}"
    return f"{', '.join(names[:-1])}, & {names[-1]}"


def first(item: dict, key: str) -> str:
    value = item.get(key)
    if isinstance(value, list) and value:
        return str(value[0])
    if value is None:
        return ""
    return str(value)


def doi_url(item: dict) -> str:
    doi = item.get("DOI")
    return f"https://doi.org/{doi}" if doi else ""


def apa_draft(item: dict) -> str:
    authors = authors_apa(item.get("author", []))
    year = year_from(item)
    title = first(item, "title").rstrip(".")
    journal = first(item, "container-title")
    volume = item.get("volume", "")
    issue = item.get("issue", "")
    page = item.get("page", "") or item.get("article-number", "")
    doi = doi_url(item)

    if journal:
        vol_issue = ""
        if volume and issue:
            vol_issue = f", {volume}({issue})"
        elif volume:
            vol_issue = f", {volume}"
        pages = f", {page}" if page else ""
        doi_part = f". {doi}" if doi else "."
        return f"{authors} ({year}). {title}. {journal}{vol_issue}{pages}{doi_part}"

    publisher = item.get("publisher", "")
    doi_part = f" {doi}" if doi else ""
    return f"{authors} ({year}). {title}. {publisher}.{doi_part}"


def simplify(item: dict) -> dict:
    return {
        "title": first(item, "title"),
        "authors": authors_apa(item.get("author", [])),
        "year": year_from(item),
        "container": first(item, "container-title"),
        "volume": item.get("volume"),
        "issue": item.get("issue"),
        "page": item.get("page") or item.get("article-number"),
        "doi": item.get("DOI"),
        "url": item.get("URL") or doi_url(item),
        "type": item.get("type"),
        "apa_draft": apa_draft(item),
    }


def lookup_doi(doi: str) -> list[dict]:
    encoded = urllib.parse.quote(doi.strip())
    data = fetch_json(f"https://api.crossref.org/works/{encoded}")
    return [data["message"]]


def lookup_title(title: str, rows: int) -> list[dict]:
    query = urllib.parse.urlencode({"query.title": title, "rows": str(rows)})
    data = fetch_json(f"https://api.crossref.org/works?{query}")
    return data["message"].get("items", [])


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--doi")
    group.add_argument("--title")
    parser.add_argument("--rows", type=int, default=5)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        items = lookup_doi(args.doi) if args.doi else lookup_title(args.title, args.rows)
    except Exception as exc:
        print(f"Crossref lookup failed: {exc}", file=sys.stderr)
        return 1

    results = [simplify(item) for item in items]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for idx, result in enumerate(results, 1):
            print(f"{idx}. {result['apa_draft']}")
            if result.get("doi"):
                print(f"   DOI: {result['doi']}")
            if result.get("url"):
                print(f"   URL: {result['url']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
