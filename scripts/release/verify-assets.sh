#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: verify-assets.sh vMAJOR.MINOR.PATCH ASSET_DIRECTORY" >&2
  exit 2
fi

tag=$1
asset_dir=$2
version=${tag#v}
wheel="$asset_dir/lsusers-${version}-py3-none-any.whl"
sdist="$asset_dir/lsusers-${version}.tar.gz"
deb="$asset_dir/lsusers_${version}-1_all.deb"

for asset in "$wheel" "$sdist" "$deb"; do
  if [[ ! -s $asset ]]; then
    echo "missing or empty release asset: $asset" >&2
    exit 1
  fi
done

if [[ $(find "$asset_dir" -maxdepth 1 -type f \
  \( -name '*.whl' -o -name '*.tar.gz' -o -name '*.deb' \) | wc -l) -ne 3 ]]; then
  echo "unexpected Python or Debian release asset" >&2
  exit 1
fi

[[ $(dpkg-deb --field "$deb" Package) == lsusers ]]
[[ $(dpkg-deb --field "$deb" Version) == "${version}-1" ]]
[[ $(dpkg-deb --field "$deb" Architecture) == all ]]

python3 - "$wheel" "$sdist" "$version" <<'PY'
import email
import io
import sys
import tarfile
import zipfile

wheel, sdist, version = sys.argv[1:]

with zipfile.ZipFile(wheel) as archive:
    metadata_paths = [name for name in archive.namelist() if name.endswith(".dist-info/METADATA")]
    if len(metadata_paths) != 1:
        raise SystemExit("wheel must contain exactly one METADATA file")
    metadata = email.message_from_bytes(archive.read(metadata_paths[0]))
    if metadata["Name"] != "lsusers" or metadata["Version"] != version:
        raise SystemExit("wheel metadata does not match the release")

with tarfile.open(sdist, "r:gz") as archive:
    pkg_info_paths = [
        name
        for name in archive.getnames()
        if name.endswith("/PKG-INFO") and name.count("/") == 1
    ]
    if len(pkg_info_paths) != 1:
        raise SystemExit("sdist must contain exactly one PKG-INFO file")
    extracted = archive.extractfile(pkg_info_paths[0])
    if extracted is None:
        raise SystemExit("could not read sdist PKG-INFO")
    metadata = email.message_from_binary_file(io.BytesIO(extracted.read()))
    if metadata["Name"] != "lsusers" or metadata["Version"] != version:
        raise SystemExit("sdist metadata does not match the release")
PY

echo "release assets match $tag"
