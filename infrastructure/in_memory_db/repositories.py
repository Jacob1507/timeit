from dataclasses import replace

from entities.task import Task
from entities.user import User


class InMemoryTaskRepository:
    def __init__(self):
        self.id_counter: int = 1
        self.tasks: dict[int, Task] = dict()

    def get_by_id(self, task_id) -> Task | None:
        return self.tasks.get(task_id)

    def get_list(self) -> list[Task]:
        return list(self.tasks.values())

    def create(self, task: Task) -> Task:
        task = replace(task, id=self.id_counter)
        self.tasks[self.id_counter] = task
        self.id_counter += 1
        return task

    def update(self, task_id: int, task: Task) -> Task | None:
        found_task: Task | None = self.tasks.get(task_id)
        if found_task is None:
            return None
        self.tasks[task_id] = replace(task, id=task_id)
        return self.tasks[task_id]

    def delete(self, task_id: int) -> bool:
        task = self.tasks.get(task_id)
        if task is None:
            return False
        del self.tasks[task_id]
        return True


class InMemoryUserRepository:
    def __init__(self):
        self.id_counter: int = 1
        self.users: dict[int, User] = dict()

    def get_by_id(self, user_id) -> User | None:
        return self.users.get(user_id)

    def get_list(self) -> list[User]:
        return list(self.users.values())

    def create(self, user: User) -> User:
        user = replace(user, id=self.id_counter)
        self.users[self.id_counter] = user
        self.id_counter += 1
        return user

    def update(self, user_id: int, user: User) -> User | None:
        found_user: User | None = self.users.get(user_id)
        if found_user is None:
            return None
        self.users[user_id] = replace(user, id=user_id)
        return self.users[user_id]

    def delete(self, user_id: int) -> bool:
        user = self.users.get(user_id)
        if user is None:
            return False
        del self.users[user_id]
        return True
