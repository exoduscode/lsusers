# Roadmap

Released work is tracked in [CHANGELOG.md](../CHANGELOG.md). This roadmap is a
direction, not a compatibility promise.

The distribution policy remains APT for Linux end users and Homebrew for macOS
end users. Python source installation is reserved for development.

## 0.1.3 — Stabilization and release automation

- Correct issues found through real-world macOS Intel and Apple Silicon use.
- Validate annotated release tags against `main`, the Python versions, the
  Debian version, and the changelog before building anything.
- Run the complete Linux, macOS ARM64, and macOS Intel matrix before building
  wheel, source distribution, and Debian artifacts from release tags.
- Build each artifact once, test those exact bytes, generate SHA-256 checksums
  and signed provenance attestations, then create the GitHub Release through a
  protected environment.
- Refuse to replace an existing GitHub Release or publish from an inconsistent
  tag.
- Open Homebrew tap update pull requests with a least-privilege credential.
- Evaluate source-built Homebrew bottles after the formula is stable.

## 0.2.0 — Filtering and output configuration

- Add `--human`, `--system`, and `--all` aliases while retaining positional
  commands.
- Add explicit minimum and maximum UID overrides with documented precedence.
- Add persistent configuration and selectable output fields.
- Version any incompatible structured-output format instead of silently
  replacing the existing JSON array.

## 0.3.0 — Read-only remote queries

- Define transport, authentication, timeouts, host-key verification, and error
  statuses before implementing remote access.
- Keep the first remote interface read-only.
- Leave account administration for a later release with a dedicated security
  model.
