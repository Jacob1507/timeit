from fastapi import APIRouter, Depends
from src.db import get_db, Database
from .schemas.task import Task


router = APIRouter(prefix="/tasks")


@router.get("/")
def get_tasks(db: Database = Depends(get_db)):
    return db.list_all()


@router.post("/")
def create_task(task: Task, db: Database = Depends(get_db)):
    return db.create(task)
