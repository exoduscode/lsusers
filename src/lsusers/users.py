from __future__ import annotations

import pwd
from typing import Iterable, List, Optional

from .models import User
from .platforms import get_account_classifier
from .platforms.linux import classify_user, read_uid_range


def list_users(
    platform_name: Optional[str] = None,
    entries: Optional[Iterable[object]] = None,
    login_defs_path: str = "/etc/login.defs",
) -> List[User]:
    account_entries = pwd.getpwall() if entries is None else entries
    classify = get_account_classifier(platform_name, login_defs_path)
    users = [
        User(
            username=entry.pw_name,
            uid=entry.pw_uid,
            gid=entry.pw_gid,
            gecos=entry.pw_gecos,
            home=entry.pw_dir,
            shell=entry.pw_shell,
            user_type=classify(entry),
        )
        for entry in account_entries
    ]
    return sorted(users, key=lambda item: (item.uid, item.username))


def filter_users(users: Iterable[User], user_type: Optional[str] = None) -> List[User]:
    result = list(users)
    if user_type:
        result = [user for user in result if user.user_type == user_type]
    return result
