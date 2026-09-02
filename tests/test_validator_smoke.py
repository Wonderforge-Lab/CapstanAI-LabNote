#!/usr/bin/env python3
"""Smoke tests for the Registry Contract v1 validator."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_repo.py"
sys.path.insert(0, str(ROOT / "scripts"))

from validate_repo import (
    validate_artifact_path_prefix,
    validate_identifier_date,
    validate_lifecycle_path,
    validate_record_type_location,
    validate_registry_inventory,
)

INVALID_FIXTURES = {
    "shared schema cannot be selected as a record": (
        "tests/fixtures/invalid/schema/common.json",
    ),
    "packet source provenance": ("tests/fixtures/invalid/packet/record.json",),
    "unknown origin disclosure": ("tests/fixtures/invalid/unknown-origin/record.json",),
    "response derivation provenance": ("tests/fixtures/invalid/response/record.json",),
    "message recipient routing": ("tests/fixtures/invalid/message/record.json",),
    "notification status vocabulary": ("tests/fixtures/invalid/notification/record.json",),
    "visit relay boolean": ("tests/fixtures/invalid/visit/record.json",),
    "visitor identifier grammar": ("tests/fixtures/invalid/visitor/record.json",),
    "accepted-tag acceptance record": ("tests/fixtures/invalid/tag/record.json",),
    "artifact path resolution": ("tests/fixtures/invalid/path/record.json",),
    "filename identifier agreement": (
        "--enforce-filename",
        "tests/fixtures/invalid/filename/not-the-packet-id.json",
    ),
    "typed reference resolution": (
        "--check-references",
        "tests/fixtures/valid/packet/record.json",
        "tests/fixtures/invalid/reference/record.json",
    ),
    "derivative reference resolution": (
        "--check-references",
        "tests/fixtures/valid/packet/record.json",
        "tests/fixtures/invalid/derivative/record.json",
    ),
    "tag vocabulary resolution": (
        "--check-tags",
        "tests/fixtures/valid/tag/record.json",
        "tests/fixtures/invalid/tag-reference/record.json",
    ),
    "lifecycle bucket agreement": (
        "--check-lifecycle",
        "tests/fixtures/invalid/lifecycle/record.json",
    ),
    "unique record identifiers": (
        "--check-unique-ids",
        "tests/fixtures/valid/packet/record.json",
        "tests/fixtures/invalid/duplicate/record.json",
    ),
}


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def assert_valid(label: str, *args: str) -> None:
    result = run(*args)
    if result.returncode != 0:
        raise AssertionError(f"{label} failed:\n{result.stdout}\n{result.stderr}")


def root_args(args: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(str(ROOT / arg) if arg.endswith(".json") else arg for arg in args)


def assert_direct_validator_invariants() -> None:
    wrong_location = validate_record_type_location(
        {"record_type": "visitor"},
        ROOT / "registry" / "packets" / "2026" / "not-a-packet.json",
        enforce=False,
    )
    if not wrong_location:
        raise AssertionError("canonical record-type location mismatch was accepted")

    wrong_date = validate_identifier_date(
        {
            "record_type": "packet",
            "packet_id": "20260901-example-topic",
            "created_at": "2026-09-02T12:00:00Z",
        },
        ROOT / "examples" / "contract_v1" / "packets" / "20260901-example-topic.json",
    )
    if not wrong_date:
        raise AssertionError("identifier/created_at date mismatch was accepted")

    wrong_year = validate_identifier_date(
        {
            "record_type": "packet",
            "packet_id": "20260902-example-topic",
            "created_at": "2026-09-02T12:00:00Z",
        },
        ROOT / "registry" / "packets" / "2025" / "20260902-example-topic.json",
    )
    if not wrong_year:
        raise AssertionError("identifier/year-directory mismatch was accepted")

    wrong_artifact_path = validate_artifact_path_prefix(
        {"record_type": "packet", "path": "AI_ENTRYPOINT.md"},
        ROOT / "registry" / "packets" / "2026" / "example.json",
    )
    if not wrong_artifact_path:
        raise AssertionError("packet artifact path outside datadrops/ was accepted")

    wrong_response_path = validate_artifact_path_prefix(
        {"record_type": "response", "path": "AI_ENTRYPOINT.md"},
        ROOT / "registry" / "responses" / "2026" / "example.json",
    )
    if not wrong_response_path:
        raise AssertionError("response artifact path outside responses/ was accepted")

    wrong_signoff_path = validate_artifact_path_prefix(
        {"record_type": "visit", "signoff_path": "responses/example.md"},
        ROOT / "registry" / "visits" / "2026" / "example.json",
    )
    if not wrong_signoff_path:
        raise AssertionError("visit signoff path outside responses/signoffs/ was accepted")

    nested_tag = validate_lifecycle_path(
        {"record_type": "tag", "status": "accepted"},
        ROOT / "registry" / "tags" / "accepted" / "sub" / "example.json",
        enforce=True,
    )
    if not nested_tag:
        raise AssertionError("nested tag record was accepted")

    with tempfile.TemporaryDirectory() as temporary:
        registry_root = Path(temporary) / "registry"
        schemas = registry_root / "schemas"
        schemas.mkdir(parents=True)
        (schemas / "common.schema.json").write_text("{}\n", encoding="utf-8")
        (registry_root / "README.md").write_text("# Registry\n", encoding="utf-8")
        (registry_root / "INDEX.md").write_text("# Index\n", encoding="utf-8")
        record = registry_root / "packets" / "2026" / "canonical.json"
        record.parent.mkdir(parents=True)
        record.write_text("{}\n", encoding="utf-8")
        (registry_root / "packets" / "2026" / "shadow.JSON").write_text(
            "{}\n", encoding="utf-8"
        )
        stray = registry_root / "inbox" / "untracked.json"
        stray.parent.mkdir()
        stray.write_text("{}\n", encoding="utf-8")
        inventory_errors = validate_registry_inventory([record], registry_root, schemas)
        if len(inventory_errors) != 2:
            raise AssertionError(
                "registry inventory did not reject uppercase and out-of-layout JSON: "
                + "\n".join(inventory_errors)
            )


def main() -> int:
    assert_direct_validator_invariants()
    assert_valid(
        "valid schema fixtures", "--fixtures", "--check-references", "--check-tags"
    )
    assert_valid(
        "contract examples", "--examples", "--check-references", "--check-tags"
    )
    assert_valid("canonical registry", "--registry")

    for invariant, args in INVALID_FIXTURES.items():
        invalid = run(*root_args(args))
        if invalid.returncode == 0:
            raise AssertionError(
                f"invalid fixture passed for {invariant}:\n{invalid.stdout}\n{invalid.stderr}"
            )

    print(f"validator smoke tests passed ({len(INVALID_FIXTURES)} invalid invariants)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
