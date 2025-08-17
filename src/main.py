from fastapi import FastAPI

from infrastructure.db import Database, db_entry
from infrastructure.in_memory_db.repositories import (
    InMemoryTaskRepository,
    InMemoryUserRepository,
)
from repositories import task, user
from src.api.routers.task import router as task_router

app = FastAPI(title="TimeIT")
app.include_router(task_router)


class Main:
    def __init__(self, app: FastAPI):
        self._app: FastAPI = app

        _task_repo = task.TaskRepository(repository=InMemoryTaskRepository())
        _user_repo = user.UserRepository(repository=InMemoryUserRepository())
        _db = Database(_task_repo, _user_repo)

        db_entry.set_db(_db)

    def __call__(self) -> FastAPI:
        return self._app


main = Main(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:main", host="0.0.0.0", port=8000, reload=True, factory=True)
