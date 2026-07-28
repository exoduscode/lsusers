from __future__ import annotations

import csv
import io
import json
from typing import Iterable

from .models import User


def as_names(users: Iterable[User]) -> str:
    return "\n".join(user.username for user in users)


def as_json(users: Iterable[User]) -> str:
    return json.dumps([user.to_dict() for user in users], ensure_ascii=False, indent=2)


def as_csv(users: Iterable[User]) -> str:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["username", "uid", "gid", "type", "home", "shell"])
    for user in users:
        writer.writerow([user.username, user.uid, user.gid, user.user_type, user.home, user.shell])
    return output.getvalue().rstrip("\n")


def as_table(users: Iterable[User]) -> str:
    rows = [[u.username, str(u.uid), u.user_type, u.home, u.shell] for u in users]
    headers = ["USER", "UID", "TYPE", "HOME", "SHELL"]
    widths = [len(value) for value in headers]
    for row in rows:
        widths = [max(width, len(value)) for width, value in zip(widths, row)]
    lines = ["  ".join(value.ljust(width) for value, width in zip(headers, widths))]
    lines.append("  ".join("-" * width for width in widths))
    lines.extend("  ".join(value.ljust(width) for value, width in zip(row, widths)) for row in rows)
    return "\n".join(lines)
