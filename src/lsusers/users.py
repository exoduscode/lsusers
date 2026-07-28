from __future__ import annotations

import pwd
from pathlib import Path
from typing import Iterable

from .models import User

DEFAULT_UID_MIN = 1000
DEFAULT_UID_MAX = 60000
NOBODY_UID = 65534


def read_uid_range(path: str = "/etc/login.defs") -> tuple[int, int]:
    uid_min = DEFAULT_UID_MIN
    uid_max = DEFAULT_UID_MAX
    try:
        for raw_line in Path(path).read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            if parts[0] == "UID_MIN":
                uid_min = int(parts[1])
            elif parts[0] == "UID_MAX":
                uid_max = int(parts[1])
    except (OSError, ValueError):
        pass
    return uid_min, uid_max


def classify_user(uid: int, uid_min: int, uid_max: int) -> str:
    if uid == 0:
        return "system"
    if uid_min <= uid <= uid_max and uid != NOBODY_UID:
        return "human"
    return "system"


def list_users() -> list[User]:
    uid_min, uid_max = read_uid_range()
    users = [
        User(
            username=entry.pw_name,
            uid=entry.pw_uid,
            gid=entry.pw_gid,
            gecos=entry.pw_gecos,
            home=entry.pw_dir,
            shell=entry.pw_shell,
            user_type=classify_user(entry.pw_uid, uid_min, uid_max),
        )
        for entry in pwd.getpwall()
    ]
    return sorted(users, key=lambda item: (item.uid, item.username))


def filter_users(users: Iterable[User], user_type: str | None = None) -> list[User]:
    result = list(users)
    if user_type:
        result = [user for user in result if user.user_type == user_type]
    return result
