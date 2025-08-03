from typing import Protocol
from ..entities.task import Task


class TaskRepository(Protocol):
    def save(self, task: Task) -> Task | None: ...

    def get(self, task_id: int) -> Task | None: ...
