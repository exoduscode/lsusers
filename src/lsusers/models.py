from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class User:
    username: str
    uid: int
    gid: int
    gecos: str
    home: str
    shell: str
    user_type: str

    def to_dict(self) -> dict:
        return asdict(self)
