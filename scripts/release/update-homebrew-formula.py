#!/usr/bin/env python3
"""Update the Homebrew formula for one immutable lsusers release."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"Homebrew formula update failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        fail(f"expected exactly one {label}")
    return updated


def main() -> None:
    if len(sys.argv) != 4:
        fail("usage: update-homebrew-formula.py FORMULA VERSION SHA256")

    formula = Path(sys.argv[1])
    version = sys.argv[2]
    checksum = sys.argv[3].lower()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        fail(f"invalid release version {version!r}")
    if not re.fullmatch(r"[0-9a-f]{64}", checksum):
        fail("SHA-256 must contain exactly 64 hexadecimal characters")
    if not formula.is_file():
        fail(f"formula does not exist: {formula}")

    text = formula.read_text(encoding="utf-8")
    text = replace_once(
        text,
        r'^  url "https://github\.com/exoduscode/lsusers/archive/refs/tags/v[^"/]+\.tar\.gz"$',
        f'  url "https://github.com/exoduscode/lsusers/archive/refs/tags/v{version}.tar.gz"',
        "source URL",
    )
    text = replace_once(
        text,
        r'^  sha256 "[^"]+"$',
        f'  sha256 "{checksum}"',
        "SHA-256",
    )
    text = replace_once(
        text,
        r'assert_match "lsusers [^"]+", shell_output\("#\{bin\}/lsusers --version"\)',
        f'assert_match "lsusers {version}", shell_output("#{{bin}}/lsusers --version")',
        "version assertion",
    )
    formula.write_text(text, encoding="utf-8")
    print(f"updated {formula} for lsusers {version}")


if __name__ == "__main__":
    main()
