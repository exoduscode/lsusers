# Output formats

All list formats preserve the same account order: UID ascending, then username
ascending.

## Table

Table output is intended for people and has five columns:

```text
USER   UID   TYPE   HOME         SHELL
-----  ----  -----  -----------  ---------
alice  1000  human  /home/alice  /bin/bash
```

Columns expand to fit their contents. Scripts should not parse this format;
use JSON, CSV, or names-only output instead. An empty result still contains the
header and separator.

## JSON

`--json` returns a UTF-8, indented JSON array. Each object has seven fields:

```json
[
  {
    "username": "alice",
    "uid": 1000,
    "gid": 1000,
    "gecos": "Alice Example",
    "home": "/home/alice",
    "shell": "/bin/bash",
    "user_type": "human"
  }
]
```

| Field | JSON type | Meaning |
|---|---|---|
| `username` | string | Login name. |
| `uid` | integer | Numeric user ID. |
| `gid` | integer | Primary numeric group ID. |
| `gecos` | string | GECOS/comment field supplied by the account database. |
| `home` | string | Configured home directory. |
| `shell` | string | Configured login shell. |
| `user_type` | string | `human` or `system`. |

Non-ASCII characters are emitted directly rather than escaped. No accounts are
represented by `[]`.

## CSV

`--csv` emits RFC-style CSV through Python's standard `csv` module:

```csv
username,uid,gid,type,home,shell
alice,1000,1000,human,/home/alice,/bin/bash
```

The columns are `username`, `uid`, `gid`, `type`, `home`, and `shell`. The GECOS
field is intentionally absent. Values containing delimiters, quotes, or line
breaks are quoted by the CSV writer. An empty result contains the header only.

## Names only

`--names` emits one username per line:

```text
alice
bob
```

An empty result produces an empty payload (the CLI's `print` still terminates
the output with a newline).

## Count

`count` has a fixed plain-text format:

```text
human: 2
system: 24
total: 26
```

The labels and ordering are stable in version 0.1.2, but this is not JSON or
CSV. Parse it only if the human-readable contract is suitable for your script.
