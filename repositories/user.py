from typing import Protocol

from entities.user import User


class UserProtocol(Protocol):
    def get_by_id(self, user_id: int) -> User | None: ...

    def get_list(self) -> list[User]: ...

    def create(self, user: User) -> User: ...

    def update(self, user_id: int, user: User) -> User | None: ...

    def delete(self, user_id: int) -> bool: ...


class UserRepository:
    def __init__(self, repository: UserProtocol):
        self.repository = repository

    def get_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)

    def get_list(self):
        return self.repository.get_list()

    def create(self, user: User):
        return self.repository.create(user)

    def update(self, user_id: int, user: User):
        return self.repository.update(user_id, user)

    def delete(self, user_id):
        return self.repository.delete(user_id)
