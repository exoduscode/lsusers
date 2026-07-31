# Command reference

## Synopsis

```text
lsusers [-h] [--json | --csv | --names] [--version]
        [{all,human,system,count}]
```

The command may appear before or after the format option.

## Commands

| Command | Behavior |
|---|---|
| `human` | List accounts classified as human by the current platform policy. This is the default. |
| `system` | List root and accounts outside the regular-user range. |
| `all` | List every account returned by the system account database. |
| `count` | Print human, system, and total counts. |

## Options

| Option | Behavior |
|---|---|
| `-h`, `--help` | Print generated command help and exit. |
| `--version` | Print `lsusers 0.1.3` and exit. |
| `--json` | Emit an indented JSON array. |
| `--csv` | Emit CSV with a header row. |
| `--names` | Emit one username per line. |

The three output options are mutually exclusive. They apply to `human`,
`system`, and `all`. `count` returns its fixed text representation even if an
output option is present.

## Defaults

- Omitted command: `human`.
- Omitted output option: aligned text table.
- Sort order: UID ascending, then username ascending.
- Linux UID range: initially 1000 through 60000, inclusive; valid values from
  `/etc/login.defs` override either boundary.
- macOS human policy: UID 500 or greater, username without `_` prefix, and a
  home directory under `/Users/`.

## Exit status

| Status | Meaning |
|---|---|
| `0` | Successful output, help, or version request. |
| `1` | The host platform is unsupported. |
| `2` | Invalid command, conflicting format options, or another argument parsing error. |

The current implementation does not define separate runtime error statuses.
On Linux, failure to read `/etc/login.defs` silently leaves the default UID
range active. Unsupported platforms return status `1` with a clear error.

## Environment and files

`lsusers` does not define environment variables or a project-specific
configuration file.

| Source | Purpose |
|---|---|
| System account database (`pwd`/NSS) | Supplies account records. |
| `/etc/login.defs` | Supplies `UID_MIN` and `UID_MAX` when readable and valid. |

## Installed interfaces

- Executable: `lsusers`
- Python module entry point: `python -m lsusers`
- Manual page: `man 1 lsusers` (Debian package)
- Bash completion: `completions/lsusers.bash`
- Zsh completion: `completions/_lsusers`
