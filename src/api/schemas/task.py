from datetime import datetime
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    user_id: int
    title: str
    completed: bool
    time: datetime
