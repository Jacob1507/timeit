from typing import Protocol

from entities.task import Task


class TaskProtocol(Protocol):
    def get_by_id(self, task_id: int) -> Task | None: ...

    def get_list(self) -> list[Task]: ...

    def create(self, task: Task) -> Task: ...

    def update(self, task_id: int, task: Task) -> Task | None: ...

    def delete(self, task_id: int) -> bool: ...


class TaskRepository:
    def __init__(self, repository: TaskProtocol):
        self.repository = repository

    def get_by_id(self, task_id: int):
        return self.repository.get_by_id(task_id)

    def get_list(self):
        return self.repository.get_list()

    def create(self, task: Task):
        return self.repository.create(task)

    def update(self, task_id: int, task: Task):
        return self.repository.update(task_id, task)

    def delete(self, task_id: int):
        return self.repository.delete(task_id)
