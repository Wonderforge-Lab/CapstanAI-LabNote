#!/usr/bin/env python3
"""Generate read-only registry views from canonical JSON records."""
from __future__ import annotations

import argparse
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
RECORD_DIRS = {
    "packet": REGISTRY / "packets",
    "response": REGISTRY / "responses",
    "message": REGISTRY / "messages",
    "notification": REGISTRY / "notifications",
    "visit": REGISTRY / "visits",
    "visitor": REGISTRY / "visitors",
    "tag": REGISTRY / "tags",
}
CSV_VIEWS = {
    "packet": ("packet_registry.csv", ["packet_id", "date", "created_at", "created_by", "deposited_by", "content_origin", "source_session", "target_session", "topic", "status", "path", "response_expected", "response_packet_id", "tags", "notes"]),
    "response": ("response_registry.csv", ["response_id", "date", "created_at", "created_by", "deposited_by", "content_origin", "responding_session", "source_packet_id", "status", "path", "accepted_by", "decision_at", "tags", "notes"]),
    "message": ("message_registry.csv", ["message_id", "date", "created_at", "from_visitor_id", "to_visitor_id", "to_group", "status", "path", "reply_to", "reply_expected", "response_message_id", "needs_human_relay", "related_packet", "related_response", "summary", "tags", "notes"]),
    "notification": ("notification_registry.csv", ["notification_id", "date", "created_at", "from_visitor_id", "to_visitor_id", "message_id", "status", "path", "needs_human_action", "summary", "notes"]),
    "visit": ("visit_registry.csv", ["visit_id", "date", "created_at", "visitor_id", "session_family", "checked_messages", "answered_messages", "created_messages", "relay_needed", "signoff_path", "notes"]),
    "visitor": ("visitor_registry.csv", ["visitor_id", "date", "created_at", "session_family", "session_type", "display_name", "status", "last_seen", "profile_path", "notes"]),
}
ID_FIELDS = {"packet": "packet_id", "response": "response_id", "message": "message_id", "notification": "notification_id", "visit": "visit_id", "visitor": "visitor_id", "tag": "tag_slug"}


def load_records() -> dict[str, list[dict]]:
    records: dict[str, list[dict]] = {record_type: [] for record_type in RECORD_DIRS}
    for expected_type, directory in RECORD_DIRS.items():
        for path in directory.rglob("*.json"):
            with path.open(encoding="utf-8") as handle:
                record = json.load(handle)
            if record.get("record_type") == expected_type:
                records[expected_type].append(record)
    for record_type, items in records.items():
        items.sort(key=lambda item: item.get(ID_FIELDS[record_type], ""))
    return records


def value(record: dict, field: str) -> str:
    if field == "date":
        created_at = record.get("created_at")
        return created_at[:10] if isinstance(created_at, str) else ""
    item = record.get(field)
    if item is None:
        return ""
    if isinstance(item, bool):
        return str(item).lower()
    if isinstance(item, list):
        return "|".join(str(entry) for entry in item)
    return str(item)


def render_csv(records: list[dict], fields: list[str]) -> str:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(fields)
    for record in records:
        writer.writerow([value(record, field) for field in fields])
    return output.getvalue()


def render_index(records: dict[str, list[dict]]) -> str:
    lines = [
        "# Registry Index",
        "",
        "> Generated from canonical JSON records by scripts/generate_registry_views.py; do not edit manually.",
        "",
        "## Record Counts",
        "",
        "| Record type | Count |",
        "| --- | ---: |",
    ]
    for record_type in ("packet", "response", "message", "notification", "visit", "visitor", "tag"):
        lines.append(f"| {record_type} | {len(records[record_type])} |")
    lines.extend(["", "## Tags", "", "| Tag | Status | Scope | Description |", "| --- | --- | --- | --- |"])
    for tag in records["tag"]:
        lines.append("| {tag_slug} | {status} | {scope} | {description} |".format(
            tag_slug=tag.get("tag_slug", ""),
            status=tag.get("status", ""),
            scope=tag.get("scope", ""),
            description=tag.get("description", "").replace("|", "\\|"),
        ))
    return "\n".join(lines) + "\n"


def generated_outputs() -> dict[Path, str]:
    records = load_records()
    outputs = {
        REGISTRY / filename: render_csv(records[record_type], fields)
        for record_type, (filename, fields) in CSV_VIEWS.items()
    }
    outputs[REGISTRY / "INDEX.md"] = render_index(records)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = generated_outputs()
    changed = [path for path, content in outputs.items() if not path.is_file() or path.read_text(encoding="utf-8") != content]
    if args.check:
        if changed:
            print("generated registry views are out of date:")
            print("\n".join(str(path.relative_to(ROOT)) for path in changed))
            return 1
        print(f"generated registry views are current ({len(outputs)} files)")
        return 0
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
    print(f"generated {len(outputs)} registry views")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
