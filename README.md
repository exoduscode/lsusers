# lsusers

<p align="center">
  <img src="docs/logo.svg" width="180" alt="lsusers">
</p>

<p align="center">
A modern Linux and macOS command-line utility for listing human, system, and all user accounts with table, JSON, CSV, and automation-friendly output.
</p>

<p align="center">
  <a href="https://github.com/exoduscode/lsusers/actions/workflows/ci.yml"><img src="https://github.com/exoduscode/lsusers/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/exoduscode/lsusers/releases"><img src="https://img.shields.io/github/v/release/exoduscode/lsusers" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/exoduscode/lsusers" alt="MIT License"></a>
</p>

## Community

- Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md).
- Report vulnerabilities according to [SECURITY.md](SECURITY.md).
- Review release history in [CHANGELOG.md](CHANGELOG.md).

---

## Features

* List human users
* List system users
* List every account known to the system account database
* Beautiful table output
* JSON output
* CSV output
* Names-only output
* Fast startup
* Script-friendly
* Debian package available
* Homebrew installation
* Linux and macOS support
* Simple command syntax

---

## Installation

For end users, the supported installation methods are **APT on Linux** and
**Homebrew on macOS**.

### Linux (APT)

Ubuntu 24.04 users configure the signed ExodusCode repository once:

```bash
curl -fsSL https://exoduscode.github.io/apt/keys/exoduscode-archive-keyring.gpg \
  | sudo tee /usr/share/keyrings/exoduscode-archive-keyring.gpg >/dev/null

sudo tee /etc/apt/sources.list.d/exoduscode.sources >/dev/null <<'EOF'
Types: deb
URIs: https://exoduscode.github.io/apt
Suites: noble
Components: main
Signed-By: /usr/share/keyrings/exoduscode-archive-keyring.gpg
EOF

sudo apt update
sudo apt install lsusers
```

Signing-key fingerprint:
`C85D DAF2 A38C A242 A745 D9DE 5A40 25DA 3610 A2EC`.

Direct installation of the release `.deb` remains available as a recovery
option for systems outside the supported repository.

---

### macOS (Homebrew)

```bash
brew install exoduscode/tap/lsusers
```

Verify the installation:

```bash
lsusers --version
```

---

### Development installation from source

The source workflow is intended for contributors and development, not as the
supported end-user installation method.

```bash
git clone https://github.com/exoduscode/lsusers.git

cd lsusers

python3 -m venv .venv

source .venv/bin/activate

pip install -e .
```

---

## Quick Start

List human users

```bash
lsusers human
```

List system users

```bash
lsusers system
```

List all users

```bash
lsusers all
```

JSON output

```bash
lsusers human --json
```

CSV output

```bash
lsusers human --csv
```

Only usernames

```bash
lsusers human --names
```

---

## Example Output

### Table

```text
USER  UID   TYPE   HOME        SHELL
----  ----  -----  ----------  ---------
matt  1000  human  /home/matt  /bin/bash
```

### JSON

```json
[
  {
    "username": "matt",
    "uid": 1000,
    "gid": 1000,
    "gecos": "Matt Abreu",
    "home": "/home/matt",
    "shell": "/bin/bash",
    "user_type": "human"
  }
]
```

### CSV

```csv
username,uid,gid,type,home,shell
matt,1000,1000,human,/home/matt,/bin/bash
```

---

## Command Reference

| Command          | Description         |
| ---------------- | ------------------- |
| `lsusers human`  | List human users    |
| `lsusers system` | List system users   |
| `lsusers all`    | List every user     |
| `lsusers count`  | Show account totals |
| `--json`         | JSON output         |
| `--csv`          | CSV output          |
| `--names`        | Usernames only      |
| `--help`         | Help                |
| `--version`      | Version information |

---

## Building the Debian Package

```bash
dpkg-buildpackage -us -uc
```

Run package validation

```bash
lintian --pedantic ../*.changes
```

---

## Running Tests

```bash
pytest
```

---

## CI

Every push is automatically validated using GitHub Actions on Linux and macOS.

The pipeline performs:

* Unit tests on Python 3.9 through 3.13
* macOS ARM64 and Intel smoke tests
* Debian package build
* Lintian validation
* Artifact publishing

---

## Roadmap

| Version | Focus |
|---|---|
| `0.1.3` | Real-world macOS fixes and release automation |
| `0.2.0` | Filters, configuration, and selectable output fields |
| `0.3.0` | Read-only remote queries |

See [CHANGELOG.md](CHANGELOG.md) for released and planned work.

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

Bug reports and feature requests are also appreciated.

---

## Security

If you discover a security issue, please report it privately before opening a public issue.

---

## License

This project is released under the MIT License.

---

## Author

**Matt Abreu**

🌐 Website
https://exoduscode.io

💼 LinkedIn
https://www.linkedin.com/in/matheusabr

🐦 X
https://x.com/mrmattabreu

🐙 GitHub
https://github.com/exoduscode

---

## Acknowledgements

Built with ❤️ for Linux and macOS users and the open-source community.
