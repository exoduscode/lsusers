# lsusers

<p align="center">
  <img src="docs/logo.svg" width="180" alt="lsusers">
</p>

<p align="center">
A modern Linux command-line utility for listing human, system, and all user accounts with beautiful table output, JSON, CSV, and automation-friendly formats.
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
* List every local user
* Beautiful table output
* JSON output
* CSV output
* Names-only output
* Fast startup
* Script-friendly
* Debian package available
* Simple command syntax

---

## Installation

### Debian Package

```bash
sudo dpkg -i lsusers_<version>_all.deb
```

If dependencies are required:

```bash
sudo apt-get install -f
```

---

### From source

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
lsusers humans
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
lsusers humans --json
```

CSV output

```bash
lsusers humans --csv
```

Only usernames

```bash
lsusers humans --names
```

---

## Example Output

### Table

```text
USERNAME    UID   HOME               SHELL
matt        1000  /home/matt         /bin/bash
john        1001  /home/john         /bin/zsh
```

### JSON

```json
[
  {
    "username": "matt",
    "uid": 1000,
    "home": "/home/matt",
    "shell": "/bin/bash"
  }
]
```

### CSV

```csv
username,uid,home,shell
matt,1000,/home/matt,/bin/bash
```

---

## Command Reference

| Command          | Description         |
| ---------------- | ------------------- |
| `lsusers humans` | List human users    |
| `lsusers system` | List system users   |
| `lsusers all`    | List every user     |
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

Every push is automatically validated using GitHub Actions.

The pipeline performs:

* Unit tests
* Debian package build
* Lintian validation
* Artifact publishing

---

## Roadmap

* Better filtering
* Group listing
* LDAP support
* Remote SSH support
* Interactive mode
* Colored output
* Package repositories (APT)
* Homebrew formula
* Snap package
* Flatpak package

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

Built with ❤️ for Linux users and the open-source community.
