#!/usr/bin/env python3
"""Validate data/conferences.json against the schema in CONTRIBUTING.md.

Standard library only. Exits non-zero and prints one line per problem.

    python3 scripts/validate_conferences.py
"""

import json
import re
import sys
from datetime import date
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

ROOT = Path(__file__).resolve().parent.parent
CONFERENCES = ROOT / "data" / "conferences.json"

KINDS = {"Conference", "Event", "Meetup", "Watch Party"}
REQUIRED = {"id", "name", "startDate", "endDate", "locationName", "summary", "websiteURL", "tags"}
OPTIONAL = {"kind", "startTime", "endTime", "timeZone", "mapQuery", "logoURL", "hasSchedule"}
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
HHMM = re.compile(r"^([01]\d|2[0-3]):[0-5]\d$")


class Report:
    def __init__(self):
        self.errors = []

    def error(self, where, message):
        self.errors.append(f"{where}: {message}")


def parse_day(value):
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def is_nonempty_string(value):
    return isinstance(value, str) and value.strip() != ""


def is_https(value):
    return isinstance(value, str) and value.startswith("https://") and len(value) > len("https://")


def validate_conference(conference, where, report):
    keys = set(conference)
    for key in sorted(REQUIRED - keys):
        report.error(where, f"missing required field `{key}`")
    for key in sorted(keys - REQUIRED - OPTIONAL):
        report.error(where, f"unknown field `{key}`")

    if not SLUG.match(str(conference.get("id", ""))):
        report.error(where, "`id` must be kebab-case (a-z, 0-9, hyphens)")
    for key in ("name", "locationName", "summary"):
        if key in conference and not is_nonempty_string(conference[key]):
            report.error(where, f"`{key}` must be a non-empty string")
    if "kind" in conference and conference["kind"] not in KINDS:
        report.error(where, f"`kind` must be one of {', '.join(sorted(KINDS))}")

    start, end = parse_day(conference.get("startDate")), parse_day(conference.get("endDate"))
    if "startDate" in conference and start is None:
        report.error(where, "`startDate` must be YYYY-MM-DD")
    if "endDate" in conference and end is None:
        report.error(where, "`endDate` must be YYYY-MM-DD")
    if start and end and end < start:
        report.error(where, "`endDate` is before `startDate`")

    for key in ("startTime", "endTime"):
        if key in conference and not (isinstance(conference[key], str) and HHMM.match(conference[key])):
            report.error(where, f"`{key}` must be 24-hour HH:mm")
    if "endTime" in conference and "startTime" not in conference:
        report.error(where, "`endTime` needs a `startTime`")
    if "timeZone" in conference:
        try:
            ZoneInfo(conference["timeZone"])
        except (ZoneInfoNotFoundError, TypeError, ValueError):
            report.error(where, "`timeZone` must be an IANA identifier, e.g. Europe/Berlin")

    if "websiteURL" in conference and not is_https(conference["websiteURL"]):
        report.error(where, "`websiteURL` must be an HTTPS URL")
    if conference.get("logoURL") not in (None, "") and not is_https(conference["logoURL"]):
        report.error(where, "`logoURL` must be an HTTPS URL, empty, or null")
    if conference.get("mapQuery") is not None and not is_nonempty_string(conference["mapQuery"]):
        report.error(where, "`mapQuery` must be a non-empty string or null")

    tags = conference.get("tags")
    if "tags" in conference and not (
        isinstance(tags, list) and tags and all(is_nonempty_string(tag) for tag in tags)
    ):
        report.error(where, "`tags` must be a non-empty list of strings")


def main():
    report = Report()
    try:
        conferences = json.loads(CONFERENCES.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(f"data/conferences.json: invalid JSON ({error})")
        return 1
    if not isinstance(conferences, list):
        print("data/conferences.json: the top level must be an array")
        return 1

    seen_ids = set()
    for index, conference in enumerate(conferences):
        if not isinstance(conference, dict):
            report.error(f"conferences.json [{index}]", "each entry must be an object")
            continue
        conference_id = conference.get("id")
        where = f"conferences.json `{conference_id}`" if conference_id else f"conferences.json [{index}]"
        if conference_id in seen_ids:
            report.error(where, "duplicate `id`")
        seen_ids.add(conference_id)
        validate_conference(conference, where, report)

    for line in report.errors:
        print(line)
    if report.errors:
        print(f"\n{len(report.errors)} problem(s) in {len(conferences)} entries.")
        return 1
    print(f"OK: {len(conferences)} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
