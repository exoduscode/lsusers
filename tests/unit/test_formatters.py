import json

from lsusers.formatters import as_csv, as_json
from lsusers.models import User


def sample_user():
    return User(
        username="alice",
        uid=1000,
        gid=1000,
        gecos="Alice Example",
        home="/home/alice",
        shell="/bin/bash",
        user_type="human",
    )


def test_json_schema_remains_an_array_of_complete_user_objects():
    payload = json.loads(as_json([sample_user()]))

    assert payload == [
        {
            "username": "alice",
            "uid": 1000,
            "gid": 1000,
            "gecos": "Alice Example",
            "home": "/home/alice",
            "shell": "/bin/bash",
            "user_type": "human",
        }
    ]


def test_csv_schema_remains_unchanged():
    assert as_csv([sample_user()]).splitlines() == [
        "username,uid,gid,type,home,shell",
        "alice,1000,1000,human,/home/alice,/bin/bash",
    ]

