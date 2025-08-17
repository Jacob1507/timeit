from typing import Protocol

from repositories.task import TaskProtocol
from repositories.user import UserProtocol


class DatabaseProtocol(Protocol):
    @property
    def task_manager(self) -> TaskProtocol: ...

    @property
    def user_manager(self) -> UserProtocol: ...


class DatabaseEntry:
    def __init__(self):
        self.db: DatabaseProtocol | None = None

    def set_db(self, db: DatabaseProtocol) -> None:
        self.db = db

    def session(self) -> DatabaseProtocol | None:
        return self.db


class Database(DatabaseProtocol):
    def __init__(self, task_repo: TaskProtocol, user_repo: UserProtocol):
        self._task_repo = task_repo
        self._user_repo = user_repo

    @property
    def task_manager(self) -> TaskProtocol:
        return self._task_repo

    @property
    def user_manager(self) -> UserProtocol:
        return self._user_repo


db_entry: DatabaseEntry = DatabaseEntry()


def get_db() -> DatabaseProtocol | None:
    assert db_entry.db is not None, "Database session is missing!"
    return db_entry.session()
