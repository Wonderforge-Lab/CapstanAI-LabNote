#!/usr/bin/env python3
"""Require a zh-CN review when a paired English source changes.

This deliberately checks review freshness, not translation quality.  It treats
the repository's current diff as the unit of work: a changed canonical source
must either change its zh-CN counterpart or receive a specific, hash-bound
review acknowledgement.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALE_ROOT = ROOT / "locales" / "zh-CN"
ACKNOWLEDGEMENTS = ROOT / "tests" / "locale_review_acknowledgements.json"

# Locale paths whose English canonical source does not follow the normal
# locales/zh-CN/<path> -> <path> relationship.
SOURCE_OVERRIDES = {
    "GLOSSARY.md": "docs/localization/GLOSSARY.md",
    "registry/TAG_DISPLAY_CATALOG.md": "docs/localization/TAG_DISPLAY_CATALOG.md",
}


def source_for_locale(relative: str) -> str:
    return SOURCE_OVERRIDES.get(relative, relative)


def locale_surfaces() -> dict[str, str]:
    surfaces: dict[str, str] = {}
    for locale_path in sorted(LOCALE_ROOT.rglob("*.md")):
        locale_rel = locale_path.relative_to(ROOT).as_posix()
        relative = locale_path.relative_to(LOCALE_ROOT).as_posix()
        surfaces[locale_rel] = source_for_locale(relative)
    return surfaces


def paired_surfaces() -> dict[str, str]:
    pairs: dict[str, str] = {}
    for locale_rel, source_rel in locale_surfaces().items():
        if (ROOT / source_rel).is_file():
            pairs[source_rel] = locale_rel
    return pairs


def files_at(revision: str) -> set[str]:
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", revision],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return {line for line in result.stdout.splitlines() if line}


def paired_surfaces_at(revision: str) -> dict[str, str]:
    files = files_at(revision)
    pairs: dict[str, str] = {}
    prefix = "locales/zh-CN/"
    for locale_rel in sorted(
        path for path in files if path.startswith(prefix) and path.endswith(".md")
    ):
        source_rel = source_for_locale(locale_rel.removeprefix(prefix))
        if source_rel in files:
            pairs[source_rel] = locale_rel
    return pairs


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def changed_paths(base: str, head: str) -> set[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", base, head],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return {line for line in result.stdout.splitlines() if line}


def acknowledgements(pairs: dict[str, str]) -> dict[str, str]:
    payload = json.loads(ACKNOWLEDGEMENTS.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise AssertionError("locale review acknowledgements require schema_version 1")

    reviewed: dict[str, str] = {}
    for entry in payload.get("acknowledgements", []):
        source = entry.get("source")
        source_sha256 = entry.get("source_sha256")
        reason = entry.get("reason")
        if not isinstance(source, str) or source not in pairs:
            raise AssertionError(f"invalid acknowledgement source: {source!r}")
        if not isinstance(source_sha256, str) or not re.fullmatch(
            r"[0-9a-f]{64}", source_sha256
        ):
            raise AssertionError(f"invalid source_sha256 for {source!r}")
        if not isinstance(reason, str) or not reason.strip():
            raise AssertionError(f"missing review reason for {source!r}")
        if source in reviewed:
            raise AssertionError(f"duplicate acknowledgement for {source!r}")
        reviewed[source] = source_sha256
    return reviewed


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: test_locale_freshness.py <base> <head>")

    pairs = paired_surfaces()
    base_pairs = paired_surfaces_at(sys.argv[1])
    changed = changed_paths(sys.argv[1], sys.argv[2])
    reviewed = acknowledgements(pairs)
    failures: list[str] = []

    for locale_rel, source_rel in locale_surfaces().items():
        if not (ROOT / source_rel).is_file():
            failures.append(
                f"localized surface has no canonical source: {locale_rel} ({source_rel})"
            )

    for source_rel, locale_rel in base_pairs.items():
        if (ROOT / source_rel).is_file() and not (ROOT / locale_rel).is_file():
            failures.append(
                f"paired localized surface was removed while its canonical source remains: "
                f"{locale_rel} ({source_rel})"
            )

    for source_rel, locale_rel in pairs.items():
        if source_rel not in changed or locale_rel in changed:
            continue
        current_digest = digest(ROOT / source_rel)
        if reviewed.get(source_rel) == current_digest:
            continue
        failures.append(
            f"{source_rel} changed without a zh-CN counterpart update or "
            f"hash-bound review acknowledgement ({locale_rel})"
        )

    if failures:
        raise AssertionError("Locale freshness check failed:\n" + "\n".join(failures))

    print(f"locale freshness check passed ({len(pairs)} paired surfaces)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
