from types import SimpleNamespace

import pytest

import lsusers.platforms
from lsusers.platforms import UnsupportedPlatformError, get_account_classifier
from lsusers.platforms.macos import classify_user as classify_macos_user
from lsusers.users import list_users


def account(username, uid, home, gid=20, gecos="", shell="/bin/zsh"):
    return SimpleNamespace(
        pw_name=username,
        pw_uid=uid,
        pw_gid=gid,
        pw_gecos=gecos,
        pw_dir=home,
        pw_shell=shell,
    )


@pytest.mark.parametrize(
    ("username", "uid", "home", "expected"),
    [
        ("alice", 501, "/Users/alice", "human"),
        ("alice", 500, "/Users/alice", "human"),
        ("_spotlight", 501, "/Users/_spotlight", "system"),
        ("daemon", 499, "/Users/daemon", "system"),
        ("network-user", 501, "/Network/Users/network-user", "system"),
    ],
)
def test_macos_classification(username, uid, home, expected):
    assert classify_macos_user(username, uid, home) == expected


def test_linux_policy_reads_configured_uid_range(tmp_path):
    login_defs = tmp_path / "login.defs"
    login_defs.write_text("UID_MIN 500\nUID_MAX 999\n", encoding="utf-8")
    classify = get_account_classifier("linux", str(login_defs))

    assert classify(account("alice", 500, "/home/alice")) == "human"
    assert classify(account("service", 1000, "/srv/service")) == "system"


def test_platform_policy_is_selected_for_macos():
    users = list_users(
        platform_name="darwin",
        entries=[account("_daemon", 600, "/Users/_daemon"), account("alice", 501, "/Users/alice")],
    )

    assert [(user.username, user.user_type) for user in users] == [
        ("alice", "human"),
        ("_daemon", "system"),
    ]


def test_host_platform_is_detected_from_sys_platform(monkeypatch):
    monkeypatch.setattr(lsusers.platforms.sys, "platform", "darwin")
    classify = get_account_classifier()

    assert classify(account("alice", 501, "/Users/alice")) == "human"


def test_unknown_platform_is_rejected():
    with pytest.raises(UnsupportedPlatformError, match="unsupported platform 'win32'"):
        get_account_classifier("win32")
