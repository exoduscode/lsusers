#!/usr/bin/env python3
"""Verify that every release-facing version agrees with a Git tag."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def fail(message: str) -> None:
    print(f"release version check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def match_one(path: str, pattern: str) -> str:
    text = (ROOT / path).read_text(encoding="utf-8")
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        fail(f"could not read version from {path}")
    return match.group(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: verify-version.py vMAJOR.MINOR.PATCH")

    tag = sys.argv[1]
    if not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", tag):
        fail(f"tag {tag!r} is not vMAJOR.MINOR.PATCH")
    version = tag.removeprefix("v")

    versions = {
        "pyproject.toml": match_one(
            "pyproject.toml",
            r"^version\s*=\s*[\"']([^\"']+)[\"']\s*$",
        ),
        "src/lsusers/__init__.py": match_one(
            "src/lsusers/__init__.py",
            r"^__version__\s*=\s*[\"']([^\"']+)[\"']\s*$",
        ),
        "debian/changelog": match_one(
            "debian/changelog",
            r"^lsusers \(([^)]+)\)",
        ).removesuffix("-1"),
        "docs/README.md": match_one(
            "docs/README.md",
            r"describes version \*\*([0-9]+\.[0-9]+\.[0-9]+)\*\*",
        ),
        "docs/cli-reference.md": match_one(
            "docs/cli-reference.md",
            r"Print `lsusers ([0-9]+\.[0-9]+\.[0-9]+)`",
        ),
        "man/lsusers.1": match_one(
            "man/lsusers.1",
            r'"lsusers ([0-9]+\.[0-9]+\.[0-9]+)" "User Commands"',
        ),
        "Homebrew formula source": match_one(
            "packaging/homebrew-tap/Formula/lsusers.rb.template",
            r"/refs/tags/v([0-9]+\.[0-9]+\.[0-9]+)\.tar\.gz",
        ),
        "Homebrew formula test": match_one(
            "packaging/homebrew-tap/Formula/lsusers.rb.template",
            r'assert_match "lsusers ([0-9]+\.[0-9]+\.[0-9]+)"',
        ),
    }

    for path, actual in versions.items():
        if actual != version:
            fail(f"{path} contains {actual!r}; expected {version!r}")

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if not re.search(rf"^## \[{re.escape(version)}\](?:\s+-\s+\d{{4}}-\d{{2}}-\d{{2}})?$", changelog, re.MULTILINE):
        fail(f"CHANGELOG.md has no release heading for {version}")

    print(f"release versions agree with {tag}")


if __name__ == "__main__":
    main()
