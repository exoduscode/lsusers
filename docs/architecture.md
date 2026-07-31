# Architecture

`lsusers` is a synchronous, dependency-free Python application. Its runtime
path is deliberately short:

```text
CLI arguments
    -> system account discovery (pwd/NSS)
    -> platform-specific classification
    -> sorting and optional filtering
    -> table, JSON, CSV, names, or count output
```

## Source layout

```text
src/lsusers/
├── __init__.py       package version
├── __main__.py       python -m lsusers entry point
├── cli.py            argument parsing and command dispatch
├── models.py         immutable User data model
├── users.py          discovery, filtering, sorting
├── platforms/        Linux and macOS classification policies
└── formatters.py     output serialization
```

Supporting areas:

```text
tests/unit/           Python unit tests
completions/          Bash and Zsh completion definitions
man/                  manual page source
debian/               Debian packaging and autopkgtests
.github/workflows/    continuous integration
```

## Module responsibilities

### `models.py`

Defines the frozen `User` dataclass with `username`, `uid`, `gid`, `gecos`,
`home`, `shell`, and `user_type`. `to_dict()` supplies the JSON representation.

### `users.py`

- `list_users()` obtains all `pwd` records, maps them to `User`, and sorts them.
- `filter_users()` optionally filters an iterable by `user_type`.

The account lookup is performed once per CLI invocation.

### `platforms/`

Selects a policy from `sys.platform`. The Linux policy reads `login.defs` once
per listing and classifies by UID. The macOS policy classifies using UID,
username, and home directory. Unsupported systems raise
`UnsupportedPlatformError`.

### `formatters.py`

Pure formatting functions accept any iterable of `User` objects and return a
string. They do not print, discover accounts, or mutate their inputs.

### `cli.py`

Builds the `argparse` parser, selects the account set, selects the formatter,
prints the result, and returns an integer process status. `count` is handled
before formatter selection.

## Data and trust boundaries

Account fields originate in the system account database and are treated as
display data. JSON and CSV use standard-library encoders. Table and names-only
formats are unescaped terminal text, so consumers handling unusual account
data should prefer JSON or CSV.

The tool is read-only: it does not modify accounts, groups, NSS configuration,
or `/etc/login.defs`.

## Python API status

Modules can be imported, and the tests use functions such as `classify_user`,
but version 0.1.3 does not declare a stable public Python API. The supported
user-facing interface is the command-line application.
