# Contributing to lsusers

Thank you for considering a contribution to `lsusers`.

## Before you start

- Search existing issues and pull requests.
- Open an issue before starting a large or behavior-changing contribution.
- Keep changes focused and backwards-compatible whenever possible.

## Development setup

```bash
git clone https://github.com/exoduscode/lsusers.git
cd lsusers
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install pytest
```

## Run tests

```bash
pytest
```

## Build the Debian package

```bash
dpkg-buildpackage -us -uc
lintian --pedantic ../lsusers_*_amd64.changes
```

## Pull requests

1. Create a branch from `main`.
2. Add or update tests when behavior changes.
3. Update documentation when commands or output change.
4. Use clear, focused commits.
5. Ensure CI passes before requesting review.

Prefer Conventional Commits, for example:

```text
feat: add group filtering
fix: handle users without home directories
docs: improve installation instructions
```

By contributing, you agree that your contribution will be licensed under the MIT License.
