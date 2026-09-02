#!/usr/bin/env python3
"""Reject a tag-slug promotion from proposed to accepted in one change set."""
from __future__ import annotations

import subprocess
import sys
from pathlib import PurePosixPath


def changed_files(base: str, head: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...{head}"],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "could not inspect change set")
    return [line for line in result.stdout.splitlines() if line]


def tag_slugs(paths: list[str], bucket: str) -> set[str]:
    prefix = PurePosixPath("registry") / "tags" / bucket
    return {
        PurePosixPath(path).stem
        for path in paths
        if PurePosixPath(path).parent == prefix and path.endswith(".json")
    }


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: check_tag_promotion.py <base-sha> <head-sha>", file=sys.stderr)
        return 2
    paths = changed_files(sys.argv[1], sys.argv[2])
    promoted = tag_slugs(paths, "proposed") & tag_slugs(paths, "accepted")
    if promoted:
        print(
            "tag promotion is not allowed in one change set: "
            + ", ".join(sorted(promoted)),
            file=sys.stderr,
        )
        return 1
    print("tag promotion separation check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
