from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str


@dataclass
class UserToken:
    user_id: int
    value: str
