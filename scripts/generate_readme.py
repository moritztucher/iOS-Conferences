#!/usr/bin/env python3
"""Regenerate the conference list in README.md from data/conferences.json.

Rewrites everything between the `conferences:start` and `conferences:end` markers:
upcoming entries grouped by month, past entries folded into a <details> block by year.
Standard library only. CI runs it on every data change and once a day, so entries
move from upcoming to past on their own.

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
    rows = ["| Date | Name | Kind | Location |", "| --- | --- | --- | --- |"]
    for entry in entries:
        when = date_range(entry["start"], entry["end"])
        if entry.get("startTime"):
            when += f", {entry['startTime']}"
        name = f"[{escape(entry['name'])}]({entry['websiteURL']})"
        rows.append(f"| {when} | {name} | {entry.get('kind', 'Conference')} | {escape(entry['locationName'])} |")
    return "\n".join(rows)


def render(conferences, today):
    for entry in conferences:
        entry["start"] = date.fromisoformat(entry["startDate"])
        entry["end"] = date.fromisoformat(entry["endDate"])
    ordered = sorted(conferences, key=lambda e: (e["start"], e.get("startTime", ""), e["name"].lower()))
    upcoming = [e for e in ordered if e["end"] >= today]
    past = [e for e in ordered if e["end"] < today][::-1]

    lines = [START_MARKER, ""]
    if upcoming:
        for (year, month), entries in groupby(upcoming, key=lambda e: (e["start"].year, e["start"].month)):
            lines += [f"### {date(year, month, 1):%B %Y}", "", table(list(entries)), ""]
    else:
        lines += ["_Nothing upcoming right now. Know of something? [Suggest it](#contributing)._", ""]

    if past:
        lines += ["<details>", f"<summary><strong>Past events ({len(past)})</strong></summary>", ""]
        for year, entries in groupby(past, key=lambda e: e["start"].year):
            lines += [f"### {year}", "", table(list(entries)), ""]
        lines += ["</details>", ""]

    lines.append(END_MARKER)
    return "\n".join(lines)


def main():
    conferences = json.loads(CONFERENCES.read_text(encoding="utf-8"))
    today = datetime.now(timezone.utc).date()
    readme = README.read_text(encoding="utf-8")
    if not BLOCK.search(readme):
        print(f"README.md: missing the {START_MARKER} / {END_MARKER} markers")
        return 1

    updated = BLOCK.sub(lambda _: render(conferences, today), readme)
    if "--check" in sys.argv:
        if updated != readme:
            print("README.md is out of date. Run: python3 scripts/generate_readme.py")
            return 1
        print("OK: README.md is up to date.")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"README.md: listed {len(conferences)} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
