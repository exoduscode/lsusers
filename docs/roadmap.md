# Roadmap

Released work is tracked in [CHANGELOG.md](../CHANGELOG.md). This roadmap is a
direction, not a compatibility promise.

The distribution policy remains APT for Linux end users and Homebrew for macOS
end users. Python source installation is reserved for development.

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
