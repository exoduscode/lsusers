# lsusers

`lsusers` is a small, read-only Linux CLI for listing user accounts with memorable commands.

## Examples

```bash
lsusers
lsusers all
lsusers system
lsusers count
lsusers --json
lsusers --csv
lsusers --names
```

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e . pytest
pytest
lsusers
```

## License

GPL-3.0-or-later.
