from datetime import datetime

from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int | None = None
    user_id: int | None = None
    title: str
    completed: bool
    time: datetime
