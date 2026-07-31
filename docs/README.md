# lsusers documentation

`lsusers` is a small, dependency-free Python command-line utility for listing
accounts known to a Linux or macOS system. It separates human and system accounts and
can produce readable tables or machine-friendly JSON, CSV, and names-only
output.

The documentation in this directory describes version **0.1.2**.

## Start here

- [Installation](installation.md) — supported environment, Debian package, and
  source installation.
- [Usage guide](usage.md) — common commands and practical examples.
- [Command reference](cli-reference.md) — every command, option, default, and
  exit status.
- [Output formats](output-formats.md) — schemas and automation examples.
- [Account classification](account-classification.md) — how `human` and
  `system` are determined.

## Maintainer documentation

- [Architecture](architecture.md) — data flow, modules, and design decisions.
- [Development and testing](development.md) — local setup, tests, and change
  checklist.
- [Debian packaging and releases](packaging.md) — package contents, build,
  validation, CI, and release procedure.
- [Troubleshooting](troubleshooting.md) — common installation and runtime
  problems.
- [Roadmap](roadmap.md) — planned stabilization, configuration, and remote
  query milestones.

## Project-level policies

The repository root contains the authoritative project policies:

- [Contributing](../CONTRIBUTING.md)
- [Security policy](../SECURITY.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [Changelog](../CHANGELOG.md)
- [License](../LICENSE)

## Quick example

```console
$ lsusers human --names
alice
bob
```

With no command, `lsusers` behaves like `lsusers human`:

```console
$ lsusers
USER   UID   TYPE   HOME         SHELL
-----  ----  -----  -----------  ---------
alice  1000  human  /home/alice  /bin/bash
```

Actual accounts and fields depend on the system account database.
