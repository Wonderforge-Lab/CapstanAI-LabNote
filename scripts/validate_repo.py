#!/usr/bin/env python3
"""Read-only Registry Contract v1 validator."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker, RefResolver

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "registry" / "schemas"
VALID_FIXTURES = ROOT / "tests" / "fixtures" / "valid"
CONTRACT_EXAMPLES = ROOT / "examples" / "contract_v1"
CANONICAL_RECORD_ROOTS = (ROOT / "registry", CONTRACT_EXAMPLES)
PATH_FIELDS = ("path", "signoff_path", "profile_path")
ID_FIELDS = {
    "packet": "packet_id",
    "response": "response_id",
    "message": "message_id",
    "notification": "notification_id",
    "visit": "visit_id",
    "visitor": "visitor_id",
    "tag": "tag_slug",
}
REFERENCE_FIELDS = {
    "packet": (("response_packet_id", "response"),),
    "response": (("source_packet_id", "packet"),),
    "message": (
        ("reply_to", "message"),
        ("response_message_id", "message"),
        ("related_packet", "packet"),
        ("related_response", "response"),
    ),
    "notification": (("message_id", "message"),),
}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def schema_for(record: dict) -> Path:
    record_type = record.get("record_type")
    if not isinstance(record_type, str):
        raise ValueError("missing or invalid record_type")
    path = SCHEMAS / f"{record_type}.schema.json"
    if not path.is_file():
        raise ValueError(f"no schema for record_type {record_type!r}")
    return path


def is_canonical_record(path: Path) -> bool:
    resolved = path.resolve()
    return any(
        resolved.is_relative_to(root.resolve()) for root in CANONICAL_RECORD_ROOTS
    )


def validate_filename(record: dict, path: Path, enforce: bool) -> list[str]:
    if not (enforce or is_canonical_record(path)):
        return []
    field = ID_FIELDS.get(record.get("record_type"))
    identifier = record.get(field) if field else None
    if isinstance(identifier, str) and path.stem != identifier:
        return [f"filename: {path.name} does not match {field} {identifier!r}"]
    return []


def validate_path_fields(record: dict) -> list[str]:
    errors: list[str] = []
    root = ROOT.resolve()
    for field in PATH_FIELDS:
        value = record.get(field)
        if value is None or not isinstance(value, str):
            continue
        target = (ROOT / value).resolve()
        try:
            target.relative_to(root)
        except ValueError:
            errors.append(f"{field}: referenced path escapes the repository")
            continue
        if not target.is_file():
            errors.append(f"{field}: referenced file does not exist: {value}")
    return errors


def validate_document(
    path: Path, enforce_filename: bool
) -> tuple[dict | None, list[str]]:
    try:
        record = load_json(path)
        schema_path = schema_for(record)
        schema = load_json(schema_path)
        resolver = RefResolver(base_uri=SCHEMAS.as_uri() + "/", referrer=schema)
        validator = Draft202012Validator(
            schema, resolver=resolver, format_checker=FormatChecker()
        )
        errors = sorted(
            validator.iter_errors(record), key=lambda error: list(error.absolute_path)
        )
        messages = [
            f"{path}: {'/'.join(map(str, error.absolute_path)) or '<record>'}: {error.message}"
            for error in errors
        ]
        messages.extend(
            f"{path}: {message}"
            for message in validate_filename(record, path, enforce_filename)
        )
        messages.extend(f"{path}: {message}" for message in validate_path_fields(record))
        return record, messages
    except (OSError, ValueError, json.JSONDecodeError) as error:
        return None, [f"{path}: {error}"]


def validate_references(records: list[tuple[Path, dict]]) -> list[str]:
    index: dict[str, set[str]] = {}
    for _, record in records:
        record_type = record.get("record_type")
        identifier_field = ID_FIELDS.get(record_type)
        identifier = record.get(identifier_field) if identifier_field else None
        if isinstance(record_type, str) and isinstance(identifier, str):
            index.setdefault(record_type, set()).add(identifier)

    errors: list[str] = []
    for path, record in records:
        record_type = record.get("record_type")
        for field, target_type in REFERENCE_FIELDS.get(record_type, ()):
            target_id = record.get(field)
            if target_id is None:
                continue
            if not isinstance(target_id, str) or target_id not in index.get(target_type, set()):
                errors.append(
                    f"{path}: {field}: no {target_type} record with ID {target_id!r} "
                    "in the validation set"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--examples", action="store_true")
    parser.add_argument("--enforce-filename", action="store_true")
    parser.add_argument("--check-references", action="store_true")
    args = parser.parse_args()

    paths = list(args.paths)
    if args.fixtures:
        paths.extend(sorted(VALID_FIXTURES.rglob("*.json")))
    if args.examples:
        paths.extend(sorted(CONTRACT_EXAMPLES.rglob("*.json")))
    if not paths:
        parser.error("supply JSON paths, --fixtures, or --examples")

    documents = [
        (path, *validate_document(path, args.enforce_filename)) for path in paths
    ]
    errors = [item for _, _, messages in documents for item in messages]
    if args.check_references:
        valid_records = [
            (path, record) for path, record, _ in documents if record is not None
        ]
        errors.extend(validate_references(valid_records))

    print("\n".join(errors) if errors else f"validated {len(paths)} record(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
