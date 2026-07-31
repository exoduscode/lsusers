import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "release" / "verify-version.py"


def project_version():
    match = re.search(
        r'^version\s*=\s*"([^"]+)"\s*$',
        (ROOT / "pyproject.toml").read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    assert match is not None
    return match.group(1)


def run_version_check(tag):
    return subprocess.run(
        [sys.executable, str(SCRIPT), tag],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_release_versions_are_synchronized():
    version = project_version()
    result = run_version_check(f"v{version}")

    assert result.returncode == 0
    assert f"release versions agree with v{version}" in result.stdout


def test_release_version_check_rejects_mismatched_tag():
    result = run_version_check("v999.999.999")

    assert result.returncode == 1
    assert "expected '999.999.999'" in result.stderr


def test_release_version_check_rejects_invalid_tag():
    result = run_version_check("release-next")

    assert result.returncode == 1
    assert "is not vMAJOR.MINOR.PATCH" in result.stderr
