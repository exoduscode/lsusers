# Installation

## Supported end-user installation methods

- Linux users install the released Debian package with APT.
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

Download the `.deb` file for the desired release, then run:

```bash
sudo apt install ./lsusers_<version>_all.deb
```

APT resolves and installs the package dependencies. Direct installation with
`dpkg -i` is not the supported end-user workflow.

Verify the installation:

```bash
lsusers --version
lsusers count
```

The Debian package also installs the manual page and Bash and Zsh completion.

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
