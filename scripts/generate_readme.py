#!/usr/bin/env python3
"""Regenerate the conference list in README.md from data/conferences.json.

Rewrites everything between the `conferences:start` and `conferences:end` markers with
conferences only (no events, meetups, or watch parties) from the current year onwards: one
table per year, each sorted by date. Standard library only. CI runs it on every data change
and on 1 January, so the previous year drops off on its own.

    python3 scripts/generate_readme.py          # rewrite README.md
    python3 scripts/generate_readme.py --check  # exit 1 if README.md is out of date
"""

import json
import re
import sys
from datetime import date, datetime, timezone
from itertools import groupby
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFERENCES = ROOT / "data" / "conferences.json"
README = ROOT / "README.md"

START_MARKER = "<!-- conferences:start -->"
END_MARKER = "<!-- conferences:end -->"
BLOCK = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)


def escape(text):
    return re.sub(r"([\\|\[\]*_<>`])", r"\\\1", text.strip())


def date_range(start, end):
    if start == end:
        return f"{start.day} {start:%b %Y}"
    if (start.year, start.month) == (end.year, end.month):
        return f"{start.day}–{end.day} {end:%b %Y}"
    if start.year == end.year:
        return f"{start.day} {start:%b} – {end.day} {end:%b %Y}"
    return f"{start.day} {start:%b %Y} – {end.day} {end:%b %Y}"


def table(entries):
    rows = ["| Date | Conference | Location |", "| --- | --- | --- |"]
    for entry in entries:
        when = date_range(entry["start"], entry["end"])
        name = f"[{escape(entry['name'])}]({entry['websiteURL']})"
        rows.append(f"| {when} | {name} | {escape(entry['locationName'])} |")
    return "\n".join(rows)


def render(conferences, current_year):
    conferences = [e for e in conferences if e.get("kind", "Conference") == "Conference"]
    for entry in conferences:
        entry["start"] = date.fromisoformat(entry["startDate"])
        entry["end"] = date.fromisoformat(entry["endDate"])
    listed = [e for e in conferences if e["start"].year >= current_year]
    by_year = sorted(listed, key=lambda e: (e["start"], e["name"].lower()))

    lines = [START_MARKER, ""]
    for year, entries in groupby(by_year, key=lambda e: e["start"].year):
        lines += [f"### {year}", "", table(list(entries)), ""]
    lines.append(END_MARKER)
    return "\n".join(lines)


def main():
    conferences = json.loads(CONFERENCES.read_text(encoding="utf-8"))
    current_year = datetime.now(timezone.utc).year
    readme = README.read_text(encoding="utf-8")
    if not BLOCK.search(readme):
        print(f"README.md: missing the {START_MARKER} / {END_MARKER} markers")
        return 1

    updated = BLOCK.sub(lambda _: render(conferences, current_year), readme)
    if "--check" in sys.argv:
        if updated != readme:
            print("README.md is out of date. Run: python3 scripts/generate_readme.py")
            return 1
        print("OK: README.md is up to date.")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"README.md: listed the conferences from {current_year} onwards.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
