# Development and testing

## Set up a development environment

```bash
git clone https://github.com/exoduscode/lsusers.git
cd lsusers
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install pytest
```

The package supports Python 3.9 and newer.

## Run the application

After an editable install:

```bash
lsusers --help
```

Without installing:

```bash
PYTHONPATH=src python3 -m lsusers --help
```

Or use:

```bash
make run
```

## Run tests

```bash
pytest
```

Equivalent repository commands are:

```bash
python3 -m pytest
make test
```

The unit suite verifies Linux UID boundaries, macOS account conventions,
platform selection, unsupported-platform errors, CLI compatibility, and output
schemas. Changes to discovery, parsing, formatting, CLI behavior, or error
handling should add focused tests for those areas.

## Manual smoke checks

Because the normal command reads the host's real account database, useful
smoke checks include:

```bash
lsusers --version
lsusers --help
lsusers human
lsusers system --names
lsusers all --json
lsusers all --csv
lsusers count
```

Do not write tests that assume a particular host has a particular username or
number of accounts. Isolate system-dependent calls when testing discovery.

## Change checklist

When changing behavior:

1. Keep command parsing, account discovery, and formatting separated.
2. Add or update tests.
3. Update the manual page and shell completions for CLI changes.
4. Update relevant files under `docs/` and the root README.
5. Add a changelog entry for user-visible changes.
6. Run the Python tests and relevant package checks.

The contribution process, commit guidance, and pull request expectations are
in [CONTRIBUTING.md](../CONTRIBUTING.md).

## Coding conventions visible in the project

- Use type annotations for function boundaries.
- Prefer standard-library facilities; runtime dependencies are currently zero.
- Return formatted strings from formatters and print only at the CLI boundary.
- Keep `User` immutable.
- Sort output deterministically.
