from pathlib import Path
from typing import Tuple

DEFAULT_UID_MIN = 1000
DEFAULT_UID_MAX = 60000
NOBODY_UID = 65534


def read_uid_range(path: str = "/etc/login.defs") -> Tuple[int, int]:
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

