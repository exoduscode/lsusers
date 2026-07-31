# Security Policy

## Security is a project requirement

Because `lsusers` is open source and distributed through privileged package
managers, security requirements are investigated for every change and are not
treated as optional follow-up work. Design, implementation, review, release,
and incident response must consider at least:

- least privilege for the CLI, CI jobs, repository tokens, and environments;
- untrusted account data, terminal output, configuration files, and platform
  differences;
- dependency and GitHub Actions provenance, vulnerability status, and update
  strategy;
- immutable tags, reproducible promotion of tested artifacts, checksums, and
  signed build provenance;
- APT and Homebrew distribution integrity, key rotation, credential scope,
  rollback, and compromise recovery;
- backwards compatibility when a security fix changes observable behavior.

Security-sensitive assumptions and residual risks must be documented. A change
must not be merged merely because no vulnerability is currently known.

## Continuous controls

- CodeQL runs for pull requests, `main`, and on a weekly schedule.
- Dependency Review rejects newly introduced dependencies with known moderate
  or higher severity vulnerabilities.
- Dependabot monitors Python build dependencies and GitHub Actions.
- Workflow permissions default to read-only and write permissions are granted
  only to the job that needs them.
- Third-party and GitHub-maintained Actions are pinned to immutable commit
  SHAs; automated updates still require CI and review.
- Releases require an annotated tag on `main`, synchronized versions, the full
  test matrix, verified artifacts, SHA-256 checksums, provenance attestations,
  and approval through a protected environment.

## Supported versions

Security fixes are provided for the latest released version of `lsusers`.

| Version | Supported |
|---|---|
| Latest release | Yes |
| Older releases | Best effort |

## Reporting a vulnerability

Do not open a public GitHub issue for a suspected vulnerability.

Use GitHub private vulnerability reporting when available. Alternatively, send
a private report to `matheusabreu.dev@gmail.com` with the affected version,
reproduction steps, potential impact, and relevant logs or proof of concept.

You should receive an acknowledgement within seven days. Please allow time for
validation and remediation before public disclosure. Do not include secrets or
personal account data unless they are essential to reproduce the issue; redact
them whenever possible.
