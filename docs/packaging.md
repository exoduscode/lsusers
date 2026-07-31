# Debian packaging and releases

Released packages are the supported user-facing distribution channels: the
signed Exoduscode APT repository serves Ubuntu 24.04, and Homebrew installs the
formula on macOS. A source or editable Python installation is a development
workflow.

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
`exoduscode/homebrew-tap` repository. For each immutable release tag, calculate
the GitHub archive SHA-256, render `Formula/lsusers.rb` from the supplied
template, and open a pull request in the tap. Its workflow audits, installs,
and runs the formula test on macOS.

## Signed APT repository

`exoduscode/apt` publishes immutable release assets through GitHub Pages at
`https://exoduscode.github.io/apt`. A protected manual workflow:

1. accepts only release tags and codenames in its manifest;
2. verifies GitHub Release state, digest, package name, version, and
   architecture;
3. rejects replacement of an existing version and version downgrades;
4. imports the package with `reprepro` and signs `Release`, `Release.gpg`, and
   `InRelease` with the dedicated archive key;
5. tests signatures, tamper rejection, installation, removal, and
   reinstallation on native AMD64 and ARM64 runners;
6. deploys only after both architectures pass.

The public archive-key fingerprint is:
`C85D DAF2 A38C A242 A745 D9DE 5A40 25DA 3610 A2EC`.

## Release checklist

The `.github/workflows/release.yml` workflow is the only supported producer of
release artifacts. An annotated `vMAJOR.MINOR.PATCH` tag must point to a commit
reachable from `main`. Before publication, the workflow:

1. verifies the tag against `pyproject.toml`, `src/lsusers/__init__.py`, the
   first Debian changelog entry, and the release heading in `CHANGELOG.md`;
2. runs the Python 3.9–3.13 matrix on Linux, macOS ARM64, and macOS Intel;
3. builds wheel, sdist, and `.deb` artifacts exactly once;
4. validates Python metadata, Debian metadata, Lintian, installation, and CLI
   smoke tests against the built files;
5. downloads the same workflow artifacts into the protected `release` job;
6. creates `SHA256SUMS` and GitHub/Sigstore provenance attestations;
7. creates the GitHub Release as a draft and publishes it only after every
   asset upload succeeds.

The workflow refuses lightweight tags, tags outside `main`, inconsistent
versions, and replacement of an existing release. Configure the GitHub
environment `release` with a required reviewer before creating the next tag.

### Operator checklist

1. Ensure user-visible behavior, docs, completions, and the manual page agree.
2. Update the version in `pyproject.toml` and `src/lsusers/__init__.py`.
3. Add the release to `CHANGELOG.md` using semantic versioning.
4. Add a matching Debian entry in `debian/changelog` and increment the Debian
   revision when appropriate.
5. Merge the release-preparation PR only after CI is green.
6. Create and push an annotated tag from the resulting `main` commit.
7. Approve the protected `release` environment after reviewing the tested
   artifacts and workflow run.
8. Verify the published checksums and provenance, for example:

   ```bash
   sha256sum --check SHA256SUMS
   gh attestation verify lsusers_<version>-1_all.deb \
     --repo exoduscode/lsusers
   ```

9. Confirm the `update-homebrew` job opened a formula PR using the tagged
   archive checksum.
10. Add the immutable `.deb` metadata and SHA-256 to the APT repository
   manifest.
11. Publish the approved tag through the protected APT production workflow.
12. Confirm project, APT, and tap GitHub Actions checks are green.
13. Verify the documented end-user commands:
    `sudo apt install lsusers` on configured Ubuntu 24.04 systems and
    `brew install exoduscode/tap/lsusers` on macOS.

The version consistency check covers Python metadata, runtime version, Debian
metadata, the changelog, CLI documentation, and both version-bearing fields in
the Homebrew formula template.

## Homebrew release automation

After GitHub Release publication, `update-homebrew` calculates the SHA-256 of
the immutable tagged source archive, updates `Formula/lsusers.rb`, and opens an
idempotent pull request in `exoduscode/homebrew-tap`. It never pushes to the
tap's default branch.

Configure a GitHub App installed only on `exoduscode/homebrew-tap`, with these
repository permissions:

- Contents: read and write;
- Pull requests: read and write;
- Metadata: read-only (implicit).

Store its ID and private key as `HOMEBREW_APP_ID` and
`HOMEBREW_APP_PRIVATE_KEY` secrets in a protected `homebrew` environment. The
workflow requests a repository-scoped installation token at runtime; no
personal access token or long-lived cross-repository token is used.
