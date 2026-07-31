# ExodusCode Homebrew tap scaffold

This directory contains the files to publish in the separate
`exoduscode/homebrew-tap` repository after the immutable `v0.1.2` tag exists.
Homebrew is the supported installation channel for macOS end users.

## Finalize the formula

Download the tagged GitHub archive and calculate its checksum:

```bash
curl -L \
  https://github.com/exoduscode/lsusers/archive/refs/tags/v0.1.2.tar.gz \
  -o lsusers-v0.1.2.tar.gz
shasum -a 256 lsusers-v0.1.2.tar.gz
```

Copy `Formula/lsusers.rb.template` to `Formula/lsusers.rb`, replace
`REPLACE_WITH_V0_1_2_ARCHIVE_SHA256` with that checksum, and do not publish the
template file in the tap.

## Validate locally

From the tap checkout:

```bash
brew tap --custom-remote exoduscode/tap "$PWD"
brew audit --strict --formula exoduscode/tap/lsusers
brew install --build-from-source exoduscode/tap/lsusers
brew test exoduscode/tap/lsusers
```

Open the first formula update as a pull request and merge it only after CI
passes. Automatic cross-repository updates are intentionally deferred.
