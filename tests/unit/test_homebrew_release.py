import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "release" / "update-homebrew-formula.py"
TEMPLATE = ROOT / "packaging" / "homebrew-tap" / "Formula" / "lsusers.rb.template"


def run_update(formula, version="0.1.3", checksum="a" * 64):
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(formula), version, checksum],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_updates_formula_release_fields(tmp_path):
    formula = tmp_path / "lsusers.rb"
    formula.write_text(TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8")

    result = run_update(formula)

    assert result.returncode == 0
    updated = formula.read_text(encoding="utf-8")
    assert "/v0.1.3.tar.gz" in updated
    assert f'  sha256 "{"a" * 64}"' in updated
    assert 'assert_match "lsusers 0.1.3"' in updated


def test_republishing_same_formula_update_is_idempotent(tmp_path):
    formula = tmp_path / "lsusers.rb"
    formula.write_text(TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8")

    first = run_update(formula)
    expected = formula.read_text(encoding="utf-8")
    second = run_update(formula)

    assert first.returncode == 0
    assert second.returncode == 0
    assert formula.read_text(encoding="utf-8") == expected


def test_rejects_invalid_version_without_modifying_formula(tmp_path):
    formula = tmp_path / "lsusers.rb"
    original = TEMPLATE.read_text(encoding="utf-8")
    formula.write_text(original, encoding="utf-8")

    result = run_update(formula, version="next")

    assert result.returncode == 1
    assert "invalid release version" in result.stderr
    assert formula.read_text(encoding="utf-8") == original


def test_rejects_invalid_checksum_without_modifying_formula(tmp_path):
    formula = tmp_path / "lsusers.rb"
    original = TEMPLATE.read_text(encoding="utf-8")
    formula.write_text(original, encoding="utf-8")

    result = run_update(formula, checksum="not-a-sha256")

    assert result.returncode == 1
    assert "SHA-256" in result.stderr
    assert formula.read_text(encoding="utf-8") == original
