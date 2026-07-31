DEFAULT_UID_MIN = 500
USER_HOME_PREFIX = "/Users/"


def classify_user(username: str, uid: int, home: str) -> str:
    if uid >= DEFAULT_UID_MIN and not username.startswith("_") and home.startswith(USER_HOME_PREFIX):
        return "human"
    return "system"

