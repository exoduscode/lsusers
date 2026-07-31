# Roadmap

Released work is tracked in [CHANGELOG.md](../CHANGELOG.md). This roadmap is a
direction, not a compatibility promise.

The distribution policy remains APT for Linux end users and Homebrew for macOS
end users. Python source installation is reserved for development.

## 0.1.3 — Stabilization and release automation

- Correct issues found through real-world macOS Intel and Apple Silicon use.
- Build wheel, source distribution, and Debian artifacts from release tags.
- Create GitHub Releases and attach verified artifacts automatically.
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
