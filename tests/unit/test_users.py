from lsusers.users import classify_user


def test_root_is_system():
    assert classify_user(0, 1000, 60000) == "system"


def test_regular_uid_is_human():
    assert classify_user(1000, 1000, 60000) == "human"


def test_low_uid_is_system():
    assert classify_user(999, 1000, 60000) == "system"


def test_nobody_is_system():
    assert classify_user(65534, 1000, 70000) == "system"
