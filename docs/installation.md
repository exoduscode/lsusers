# Installation

## Supported end-user installation methods

- Ubuntu 24.04 users install from the signed ExodusCode APT repository.
- macOS users install the formula from the ExodusCode Homebrew tap.

Installing from source is documented for contributors and development only.

## Requirements

`lsusers` requires:

- Linux or macOS with Python's `pwd` module;
- Python 3.9 or newer for source installations;
- no third-party Python runtime dependencies.

The application reads the system account database through the operating
system. It does not need root privileges.

## Linux: install with APT

The signed repository currently supports Ubuntu 24.04 (`noble`) on AMD64 and
ARM64. Configure it once without using the deprecated `apt-key` mechanism:

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

Verify the complete signing-key fingerprint before trusting it:

```text
C85D DAF2 A38C A242 A745 D9DE 5A40 25DA 3610 A2EC
```

Future releases are delivered through normal APT upgrades:

```bash
sudo apt update
sudo apt upgrade
```

Verify the installation:

```bash
lsusers --version
lsusers count
```

The Debian package also installs the manual page and Bash and Zsh completion.

### Recovery installation

For unsupported distributions or repository recovery, download the `.deb`
from the corresponding GitHub Release and install the local file:

```bash
sudo apt install ./lsusers_<version>_all.deb
```

This bypasses automatic discovery of future releases and is not the primary
Ubuntu 24.04 installation path.

## macOS: install with Homebrew

On macOS, install from the ExodusCode tap:

```bash
brew install exoduscode/tap/lsusers
```

Then verify the formula:

```bash
lsusers --version
brew test exoduscode/tap/lsusers
```

## Development installation from source

This workflow is for contributors and local development. Clone the repository
and create an isolated environment:

```bash
git clone https://github.com/exoduscode/lsusers.git
cd lsusers
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

An editable install is convenient for development. For a regular local
install, omit `-e`:

```bash
python -m pip install .
```

Verify it with:

```bash
lsusers --version
python -m lsusers --version
```

Both entry points invoke the same CLI.

## Run without installing

From the repository root:

```bash
PYTHONPATH=src python3 -m lsusers
```

The Makefile provides the same development shortcut:

```bash
make run
```

## Uninstall

For a development Python installation:

```bash
python -m pip uninstall lsusers
```

For a Debian installation:

```bash
sudo apt remove lsusers
```

For a Homebrew installation:

```bash
brew uninstall lsusers
```
