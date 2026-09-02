#!/usr/bin/env python3
"""Read-only Registry Contract v1 validator."""
from __future__ import annotations

import argparse
import json
import re
from functools import lru_cache
from pathlib import Path, PurePosixPath

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_ROOT = ROOT / "registry"
SCHEMAS = REGISTRY_ROOT / "schemas"
REGISTRY_RECORD_DIRS = (
    REGISTRY_ROOT / "packets",
    REGISTRY_ROOT / "responses",
    REGISTRY_ROOT / "messages",
    REGISTRY_ROOT / "notifications",
    REGISTRY_ROOT / "visits",
    REGISTRY_ROOT / "visitors",
    REGISTRY_ROOT / "tags",
)
VALID_FIXTURES = ROOT / "tests" / "fixtures" / "valid"
CONTRACT_EXAMPLES = ROOT / "examples" / "contract_v1"
CANONICAL_RECORD_ROOTS = (REGISTRY_ROOT, CONTRACT_EXAMPLES)
PATH_FIELDS = ("path", "signoff_path", "profile_path")
ARTIFACT_PATH_PREFIXES = {
    "packet": ("path", PurePosixPath("datadrops")),
    "response": ("path", PurePosixPath("responses")),
    "visit": ("signoff_path", PurePosixPath("responses") / "signoffs"),
}
GENERATED_REGISTRY_VIEWS = frozenset(
    {
        "INDEX.md",
        "packet_registry.csv",
        "response_registry.csv",
        "message_registry.csv",
        "notification_registry.csv",
        "visit_registry.csv",
        "visitor_registry.csv",
    }
)
ID_FIELDS = {
    "packet": "packet_id",
    "response": "response_id",
    "message": "message_id",
    "notification": "notification_id",
    "visit": "visit_id",
    "visitor": "visitor_id",
    "tag": "tag_slug",
}
RECORD_TYPES = frozenset(ID_FIELDS)
RECORD_TYPE_DIRS = {
    "packets": "packet",
    "responses": "response",
    "messages": "message",
    "notifications": "notification",
    "visits": "visit",
    "visitors": "visitor",
    "tags": "tag",
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
DERIVATIVE_TYPES = frozenset({"packet", "response"})
MESSAGE_BUCKETS = {
    "open": "open",
    "acknowledged": "open",
    "in_progress": "open",
    "blocked": "open",
    "answered": "answered",
    "closed": "closed",
    "archived": "archived",
}
NOTIFICATION_BUCKETS = {
    "needed": "open",
    "told_to_human": "open",
    "delivered_by_human": "delivered",
    "confirmed": "closed",
    "cancelled": "closed",
}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


@lru_cache
def schema_registry() -> Registry:
    resources = [
        (path.name, Resource.from_contents(load_json(path)))
        for path in sorted(SCHEMAS.glob("*.schema.json"))
    ]
    return Registry().with_resources(resources)


def schema_for(record: dict) -> Path:
    record_type = record.get("record_type")
    if not isinstance(record_type, str):
        raise ValueError("missing or invalid record_type")
    if record_type not in RECORD_TYPES:
        raise ValueError(f"{record_type!r} is not a Registry Contract record type")
    path = SCHEMAS / f"{record_type}.schema.json"
    if not path.is_file():
        raise ValueError(f"no schema for record_type {record_type!r}")
    return path


def is_under(path: Path, root: Path) -> bool:
    return path.resolve().is_relative_to(root.resolve())


def is_canonical_record(path: Path) -> bool:
    return any(is_under(path, root) for root in CANONICAL_RECORD_ROOTS)


def expected_record_type(path: Path) -> str | None:
    resolved = path.resolve()
    for root in CANONICAL_RECORD_ROOTS:
        try:
            relative = resolved.relative_to(root.resolve())
        except ValueError:
            continue
        for part in relative.parts:
            record_type = RECORD_TYPE_DIRS.get(part)
            if record_type is not None:
                return record_type
    return None


def validate_record_type_location(record: dict, path: Path, enforce: bool) -> list[str]:
    if not (enforce or is_canonical_record(path)):
        return []
    expected = expected_record_type(path)
    if expected is None:
        return []
    actual = record.get("record_type")
    if actual != expected:
        return [
            f"record_type: {actual!r} does not match canonical directory "
            f"(expected {expected!r})"
        ]
    return []


def validate_filename(record: dict, path: Path, enforce: bool) -> list[str]:
    if not (enforce or is_canonical_record(path)):
        return []
    field = ID_FIELDS.get(record.get("record_type"))
    identifier = record.get(field) if field else None
    if isinstance(identifier, str) and path.stem != identifier:
        return [f"filename: {path.name} does not match {field} {identifier!r}"]
    return []


def identifier_date(record: dict) -> str | None:
    record_type = record.get("record_type")
    identifier_field = ID_FIELDS.get(record_type)
    identifier = record.get(identifier_field) if identifier_field else None
    if not isinstance(identifier, str):
        return None
    if record_type == "visitor":
        match = re.search(r"-([0-9]{8})-[0-9]{4}-", identifier)
    elif record_type == "tag":
        return None
    else:
        match = re.match(r"([0-9]{8})-", identifier)
    return match.group(1) if match else None


def validate_identifier_date(record: dict, path: Path) -> list[str]:
    identifier_day = identifier_date(record)
    created_at = record.get("created_at")
    if identifier_day is None or not isinstance(created_at, str):
        return []
    created_day = created_at[:10].replace("-", "")
    if not re.fullmatch(r"[0-9]{8}", created_day):
        return []

    errors: list[str] = []
    if identifier_day != created_day:
        errors.append(
            f"identifier date {identifier_day!r} does not match created_at date {created_day!r}"
        )

    if is_under(path, REGISTRY_ROOT):
        relative = path.resolve().relative_to(REGISTRY_ROOT.resolve())
        year_directories = [part for part in relative.parts if re.fullmatch(r"[0-9]{4}", part)]
        for year in year_directories:
            if year != created_day[:4]:
                errors.append(
                    f"year directory {year!r} does not match created_at year {created_day[:4]!r}"
                )
    return errors


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


def validate_artifact_path_prefix(record: dict, location: Path) -> list[str]:
    """Keep canonical artifact records out of control-plane and unrelated paths."""
    if not is_under(location, REGISTRY_ROOT):
        return []
    constraint = ARTIFACT_PATH_PREFIXES.get(record.get("record_type"))
    if constraint is None:
        return []
    field, prefix = constraint
    value = record.get(field)
    if value is None or not isinstance(value, str):
        return []
    path = PurePosixPath(value)
    if not path.is_relative_to(prefix):
        return [f"{field}: {record['record_type']} artifacts must be under {prefix}/"]
    return []


def validate_lifecycle_path(record: dict, location: Path, enforce: bool) -> list[str]:
    if not (enforce or is_under(location, REGISTRY_ROOT)):
        return []
    record_type = record.get("record_type")
    status = record.get("status")
    if record_type == "message":
        bucket = MESSAGE_BUCKETS.get(status)
        if bucket is None:
            return []
        record_prefix = Path("registry") / "messages" / bucket
        artifact_prefix = Path("messages") / bucket
    elif record_type == "notification":
        bucket = NOTIFICATION_BUCKETS.get(status)
        if bucket is None:
            return []
        record_prefix = Path("registry") / "notifications" / bucket
        artifact_prefix = Path("notifications") / bucket
    elif record_type == "tag" and status in {"proposed", "accepted", "deprecated"}:
        record_prefix = Path("registry") / "tags" / status
        artifact_prefix = None
    else:
        return []

    errors: list[str] = []
    try:
        relative_location = location.resolve().relative_to(ROOT.resolve())
        if record_type == "tag" and relative_location.parent != record_prefix:
            errors.append(
                f"lifecycle: tag status {status!r} requires a direct record under "
                f"{record_prefix}/"
            )
        elif not relative_location.is_relative_to(record_prefix):
            errors.append(
                f"lifecycle: status {status!r} requires record location under {record_prefix}/"
            )
    except ValueError:
        errors.append("lifecycle: record location escapes the repository")

    artifact_path = record.get("path")
    if artifact_prefix is not None and isinstance(artifact_path, str):
        if not Path(artifact_path).is_relative_to(artifact_prefix):
            errors.append(
                f"lifecycle: status {status!r} requires artifact path under {artifact_prefix}/"
            )
    return errors


def validate_document(
    path: Path, enforce_filename: bool, check_lifecycle: bool
) -> tuple[dict | None, list[str]]:
    try:
        record = load_json(path)
        schema_path = schema_for(record)
        schema = load_json(schema_path)
        validator = Draft202012Validator(
            schema, registry=schema_registry(), format_checker=FormatChecker()
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
            for message in validate_record_type_location(record, path, enforce_filename)
        )
        messages.extend(
            f"{path}: {message}"
            for message in validate_filename(record, path, enforce_filename)
        )
        messages.extend(
            f"{path}: {message}" for message in validate_identifier_date(record, path)
        )
        messages.extend(f"{path}: {message}" for message in validate_path_fields(record))
        messages.extend(
            f"{path}: {message}"
            for message in validate_artifact_path_prefix(record, path)
        )
        messages.extend(
            f"{path}: {message}"
            for message in validate_lifecycle_path(record, path, check_lifecycle)
        )
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
        if record_type in DERIVATIVE_TYPES:
            derivatives = record.get("derivative_of")
            if isinstance(derivatives, list):
                for derivative in derivatives:
                    if not isinstance(derivative, str) or not any(
                        derivative in index.get(target_type, set())
                        for target_type in DERIVATIVE_TYPES
                    ):
                        errors.append(
                            f"{path}: derivative_of: no packet or response record with ID "
                            f"{derivative!r} in the validation set"
                        )
    return errors


def validate_unique_ids(records: list[tuple[Path, dict]]) -> list[str]:
    locations: dict[tuple[str, str], list[Path]] = {}
    for path, record in records:
        record_type = record.get("record_type")
        identifier_field = ID_FIELDS.get(record_type)
        identifier = record.get(identifier_field) if identifier_field else None
        if isinstance(record_type, str) and isinstance(identifier, str):
            locations.setdefault((record_type, identifier), []).append(path)

    return [
        f"duplicate {record_type} ID {identifier!r}: "
        + ", ".join(str(path) for path in paths)
        for (record_type, identifier), paths in locations.items()
        if len(paths) > 1
    ]


def validate_tags(records: list[tuple[Path, dict]]) -> list[str]:
    available = {
        record["tag_slug"]
        for _, record in records
        if record.get("record_type") == "tag"
        and record.get("status") in {"proposed", "accepted"}
        and isinstance(record.get("tag_slug"), str)
    }
    errors: list[str] = []
    for path, record in records:
        tags = record.get("tags")
        if not isinstance(tags, list):
            continue
        for tag in tags:
            if not isinstance(tag, str) or tag not in available:
                errors.append(
                    f"{path}: tags: no proposed or accepted tag record for {tag!r} "
                    "in the validation set"
                )
    return errors


def registry_paths() -> list[Path]:
    return sorted(
        path for directory in REGISTRY_RECORD_DIRS for path in directory.rglob("*.json")
    )


def validate_registry_inventory(
    record_paths: list[Path], registry_root: Path = REGISTRY_ROOT, schemas: Path = SCHEMAS
) -> list[str]:
    """Reject registry files that are neither contract support nor validated records."""
    known_records = {path.resolve() for path in record_paths}
    errors: list[str] = []
    for path in sorted(candidate for candidate in registry_root.rglob("*") if candidate.is_file()):
        relative = path.resolve().relative_to(registry_root.resolve())
        if path.name == ".gitkeep":
            continue
        if is_under(path, schemas) and path.name.endswith(".schema.json"):
            continue
        if relative.parent == Path(".") and path.name in GENERATED_REGISTRY_VIEWS | {"README.md"}:
            continue
        if path.resolve() in known_records:
            continue
        errors.append(f"{path}: registry inventory contains an unvalidated or unsupported file")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--examples", action="store_true")
    parser.add_argument("--registry", action="store_true")
    parser.add_argument("--enforce-filename", action="store_true")
    parser.add_argument("--check-references", action="store_true")
    parser.add_argument("--check-tags", action="store_true")
    parser.add_argument("--check-lifecycle", action="store_true")
    parser.add_argument("--check-unique-ids", action="store_true")
    args = parser.parse_args()

    paths = list(args.paths)
    if args.fixtures:
        paths.extend(sorted(VALID_FIXTURES.rglob("*.json")))
    if args.examples:
        paths.extend(sorted(CONTRACT_EXAMPLES.rglob("*.json")))
    if args.registry:
        paths.extend(registry_paths())
    if not paths:
        parser.error("supply JSON paths, --fixtures, --examples, or --registry")

    enforce_filename = args.enforce_filename or args.registry
    check_references = args.check_references or args.registry
    check_tags = args.check_tags or args.registry
    check_lifecycle = args.check_lifecycle or args.registry
    check_unique_ids = args.check_unique_ids or args.registry
    documents = [
        (path, *validate_document(path, enforce_filename, check_lifecycle))
        for path in paths
    ]
    errors = [item for _, _, messages in documents for item in messages]
    valid_records = [
        (path, record) for path, record, _ in documents if record is not None
    ]
    if check_references:
        errors.extend(validate_references(valid_records))
    if check_tags:
        errors.extend(validate_tags(valid_records))
    if check_unique_ids:
        errors.extend(validate_unique_ids(valid_records))
    if args.registry:
        errors.extend(validate_registry_inventory(paths))

    print("\n".join(errors) if errors else f"validated {len(paths)} record(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
