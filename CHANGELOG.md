# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.3] - 2026-07-31

### Added

- Signed Exoduscode APT repository documentation for Ubuntu 24.04.
- Tag-gated release workflow that tests, builds, verifies, attests, and
  publishes wheel, source, and Debian artifacts without rebuilding them.
- SHA-256 manifest and automated release-version consistency checks.
- Continuous CodeQL, dependency review, and Dependabot security controls.
- Automated Homebrew tap update pull requests authenticated by a
  least-privilege GitHub App.

### Changed

- GitHub Actions dependencies are pinned to immutable commit SHAs.
- Security investigation and least privilege are explicit acceptance criteria
  for every project change.
- CodeQL updates are applied as one audited version change instead of separate
  digest-only Dependabot pull requests.

## [0.1.2] - 2026-07-31

### Added

- Official macOS support with platform-specific account classification.
- CI coverage for Python 3.9 through 3.13 on Linux, macOS ARM64, and macOS Intel.
- Homebrew tap formula and validation workflow template.

### Changed

- Updated project and Debian metadata to consistently use the MIT license.
- Updated documentation and descriptions for Linux and macOS.

## [0.1.1] - 2026-07-31

### Changed

- Updated Debian package maintainer metadata.
- Updated the author's X profile link.
- Improved public project metadata.

## [0.1.0] - 2026-07-31

### Added

- Human, system, and all-user listing commands.
- Table, JSON, CSV, and names-only output.
- Debian package support.
- Automated tests and GitHub Actions CI.

[Unreleased]: https://github.com/exoduscode/lsusers/compare/v0.1.3...HEAD
[0.1.3]: https://github.com/exoduscode/lsusers/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/exoduscode/lsusers/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/exoduscode/lsusers/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/exoduscode/lsusers/releases/tag/v0.1.0
