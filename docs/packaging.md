# Debian packaging and releases

Released packages are the supported user-facing distribution channels: APT
installs the `.deb` on Linux, and Homebrew installs the formula on macOS. A
source or editable Python installation is a development workflow.

## Package contents

The Debian package is architecture-independent (`Architecture: all`) and
installs:

- the Python package and `lsusers` executable;
- the `lsusers(1)` manual page;
- Bash completion;
- Zsh completion.

Package metadata lives under `debian/`. The build uses debhelper 13, `dh`, and
the `pybuild` PEP 517 build system.

## Build dependencies

On an Ubuntu or Debian build host, install the tools represented in
`debian/control` and CI:

```bash
sudo apt-get update
sudo apt-get install -y \
  build-essential debhelper devscripts dh-python lintian \
  pybuild-plugin-pyproject python3-all python3-pytest python3-setuptools
```

## Build

From the repository root:

```bash
dpkg-buildpackage -us -uc -b
```

Or:

```bash
make build-deb
```

Debian build artifacts are written to the parent directory. The build runs the
Python test suite through `override_dh_auto_test`.

## Validate

Run Lintian against the generated changes file:

```bash
lintian --display-info --display-experimental --pedantic \
  ../lsusers_*_amd64.changes
```

Inspect the package and perform an installation smoke test in a disposable
environment when possible:

```bash
dpkg-deb --info ../lsusers_*_all.deb
dpkg-deb --contents ../lsusers_*_all.deb
```

The package defines a superficial autopkgtest that verifies executable
discovery, help, version, default listing, `count`, and names output.

## Continuous integration

`.github/workflows/ci.yml` runs on pushes to `main`, pull requests, and manual
dispatch. Its portable test matrix covers Python 3.9 through 3.13 on Ubuntu
24.04, macOS ARM64, and macOS Intel. A separate Ubuntu job:

1. installs Debian build dependencies;
2. builds and tests the binary Debian package;
3. runs Lintian in pedantic mode;
4. uploads the `.deb` as the `lsusers-deb` workflow artifact.

## Homebrew tap

The `packaging/homebrew-tap/` scaffold is intended for the separate
`exoduscode/homebrew-tap` repository. After the `v0.1.2` tag exists, calculate
the GitHub archive SHA-256, render `Formula/lsusers.rb` from the supplied
template, and open a pull request in the tap. Its workflow audits, installs,
and runs the formula test on macOS.

## Release checklist

1. Ensure user-visible behavior, docs, completions, and the manual page agree.
2. Update the version in `pyproject.toml` and `src/lsusers/__init__.py`.
3. Add the release to `CHANGELOG.md` using semantic versioning.
4. Add a matching Debian entry in `debian/changelog` and increment the Debian
   revision when appropriate.
5. Run tests, build the package, and run Lintian.
6. Verify `lsusers --version` from the built package.
7. Tag the release and publish the `.deb` and relevant source artifacts.
8. Calculate the tagged archive checksum and finalize the Homebrew formula.
9. Confirm project and tap GitHub Actions checks are green.
10. Verify the documented end-user commands:
    `sudo apt install ./lsusers_<version>_all.deb` on Linux and
    `brew install exoduscode/tap/lsusers` on macOS.

Version values are currently duplicated, so keeping them synchronized is a
manual release responsibility.
