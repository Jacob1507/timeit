from fastapi import APIRouter, Depends

from entities.task import Task
from infrastructure.db import DatabaseProtocol, get_db
from src.api.schemas.task import TaskSchema

router = APIRouter(prefix="/tasks")


@router.get("/", name="task_list")
def task_list(db: DatabaseProtocol = Depends(get_db)):
    return db.task_manager.get_list()


@router.post("/", name="task_create")
def task_create(task_schema: TaskSchema, db: DatabaseProtocol = Depends(get_db)):
    task = Task(**task_schema.model_dump())
    return db.task_manager.create(task)


@router.get("/{task_id}", name="task_detail")
def task_detail(task_id: int, db: DatabaseProtocol = Depends(get_db)):
    return db.task_manager.get_by_id(task_id)


@router.put("/{task_id}", name="task_update")
def task_update(
    task_id: int, task_schema: TaskSchema, db: DatabaseProtocol = Depends(get_db)
):
    task = Task(**task_schema.model_dump())
    return db.task_manager.update(task_id, task)


@router.delete("/{task_id}", name="task_delete")
def task_delete(task_id: int, db: DatabaseProtocol = Depends(get_db)):
    return db.task_manager.delete(task_id)
