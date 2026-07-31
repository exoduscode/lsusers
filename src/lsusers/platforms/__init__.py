from __future__ import annotations

import sys
from typing import Any, Callable, Optional

from . import linux, macos


class UnsupportedPlatformError(RuntimeError):
    """Raised when lsusers has no account classification policy for the host."""


def get_account_classifier(
    platform_name: Optional[str] = None,
    login_defs_path: str = "/etc/login.defs",
) -> Callable[[Any], str]:
    """Build an account classifier for the selected host platform."""

    selected_platform = platform_name if platform_name is not None else sys.platform

    if selected_platform.startswith("linux"):
        uid_min, uid_max = linux.read_uid_range(login_defs_path)
        return lambda account: linux.classify_user(account.pw_uid, uid_min, uid_max)
    if selected_platform == "darwin":
        return lambda account: macos.classify_user(
            account.pw_name, account.pw_uid, account.pw_dir
        )

    raise UnsupportedPlatformError(
        "unsupported platform {!r}; supported platforms: linux, darwin".format(selected_platform)
    )


def classify_account(
    account: Any,
    platform_name: Optional[str] = None,
    login_defs_path: str = "/etc/login.defs",
) -> str:
    """Classify one pwd-compatible account using the host platform policy."""

    return get_account_classifier(platform_name, login_defs_path)(account)
