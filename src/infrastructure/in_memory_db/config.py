from ...entities.task import Task


class Database:
    def __init__(self):
        self._counter = 1
        self._db = dict()
    
    def disconnect(self):
        self._db = dict()
        self._counter = 1
    
    def get(self, task_id: int) -> Task | None:
        return self._db.get(task_id)

    def create(self, task: Task) -> Task:
        task.id = self._counter
        self._db[task.id] = task
        self._counter += 1
        return task

    def list_all(self) -> list[Task]:
        return list(self._db.values())
