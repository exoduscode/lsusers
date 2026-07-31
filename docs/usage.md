# Usage guide

The general syntax is:

```text
lsusers [command] [--json | --csv | --names]
```

## Select accounts

List human accounts (the default):

```bash
lsusers
lsusers human
```

List system accounts:

```bash
lsusers system
```

List every account:

```bash
lsusers all
```

Show category totals:

```bash
lsusers count
```

Example:

```text
human: 2
system: 24
total: 26
```

The project uses `human` in the singular. `humans` is not a valid command.

## Select an output format

Table output is used when no format option is supplied:

```bash
lsusers human
```

For structured or compact output:

```bash
lsusers all --json
lsusers system --csv
lsusers human --names
```

`--json`, `--csv`, and `--names` are mutually exclusive. The `count` command
always prints its three-line text summary; format options do not change it.

## Common automation recipes

Count human usernames with standard shell tools:

```bash
lsusers human --names | wc -l
```

Test whether a human account is present:

```bash
lsusers human --names | grep -Fxq 'alice'
```

Read JSON with `jq`:

```bash
lsusers all --json | jq '.[] | select(.shell == "/bin/bash")'
```

Select CSV columns with a CSV-aware tool. Avoid splitting CSV on commas in
shell code because fields can require quoting.

## Discover accounts and ordering

Accounts come from Python's `pwd.getpwall()`, which uses the system's account
database. On Linux, depending on `/etc/nsswitch.conf`, results may include
sources other than `/etc/passwd`, such as LDAP or SSSD.

Results are sorted by numeric UID, then by username. The tool does not check
whether a home directory or shell exists, whether a shell is interactive, or
whether an account is currently logged in.
