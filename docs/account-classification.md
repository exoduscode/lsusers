# Account classification

`lsusers` selects a classification policy from `sys.platform`. Linux and
macOS are supported. Other platforms stop with a clear error instead of using
an incorrect fallback policy.

## Linux

Linux classification uses numeric UID only. At startup, the application reads
`/etc/login.defs` and looks for:

```text
UID_MIN 1000
UID_MAX 60000
```

The reader starts with `UID_MIN = 1000` and `UID_MAX = 60000`. Valid settings
replace the corresponding defaults. If the file cannot be read, both defaults
remain. An invalid integer stops further parsing; values already read are
retained. The limits are inclusive.

The rules are:

```text
uid == 0                          -> system
UID_MIN <= uid <= UID_MAX
  and uid != 65534               -> human
otherwise                         -> system
```

UID `65534` (`nobody`) is always a system account.

## macOS

A macOS account is classified as human only when all three conditions hold:

```text
uid >= 500
username does not start with "_"
home starts with "/Users/"
```

Every other account is classified as system. Shell values do not affect the
result.

## Consequences

- Classification describes common platform conventions, not identity or
  authorization.
- A service account inside a Linux regular-user UID range can be reported as
  human.
- A macOS network account whose home is outside `/Users/` is reported as
  system.
- Linux NSS and macOS directory services may supply accounts that do not
  follow local allocation conventions.

Do not use these labels alone to grant access or privileges.
