# Troubleshooting

## `lsusers: command not found`

Confirm the package is installed in the active environment:

```bash
python -m pip show lsusers
python -m lsusers --version
```

If `python -m lsusers` works but `lsusers` does not, activate the virtual
environment or ensure its `bin` directory is on `PATH`.

## `invalid choice: 'humans'`

The supported command is singular:

```bash
lsusers human
```

Running `lsusers` with no command has the same behavior.

## Conflicting output options

Only one output option may be used at a time:

```bash
lsusers all --json
```

A command such as `lsusers all --json --csv` is rejected with exit status 2.

## An account is in the unexpected category

On Linux, check its UID and the local allocation range:

```bash
getent passwd ACCOUNT_NAME
grep -E '^[[:space:]]*UID_(MIN|MAX)[[:space:]]' /etc/login.defs
```

Linux classification is based only on UID. See
[Account classification](account-classification.md) for the exact rules.

On macOS, username and home directory also participate in classification. A
human account must have UID 500 or greater, no `_` prefix, and a home below
`/Users/`.

## Results differ from `/etc/passwd`

This can be expected. `lsusers` uses the system account database through NSS,
which may combine local files with services such as LDAP or SSSD. Inspect the
`passwd` entry in `/etc/nsswitch.conf` and compare with:

```bash
getent passwd
```

Remote directory availability and NSS caching can affect results.

## JSON has more fields than CSV or table output

The formats intentionally expose different views:

- JSON includes all seven `User` fields, including GECOS.
- CSV omits GECOS and uses `type` as the classification column name.
- The table omits GID and GECOS.
- Names-only output contains only usernames.

See [Output formats](output-formats.md) for the schemas.

## `count --json` is not JSON

In version 0.1.3, `count` always uses its fixed plain-text output and does not
apply output format flags. Use list JSON and calculate the desired count with a
JSON processor when structured output is required.

## Debian build fails

Install all build dependencies listed in [Packaging](packaging.md), then retry
from a clean source tree. To remove generated local build files with the
project's Makefile:

```bash
make clean
```

Review the first failing `dpkg-buildpackage`, test, or Lintian message rather
than only the final summary.

## Reporting bugs and vulnerabilities

Open regular bugs and feature requests in the project issue tracker. Security
issues must be reported privately as described in
[SECURITY.md](../SECURITY.md); do not publish vulnerability details in an
issue.
