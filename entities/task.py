from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    user_id: int
    title: str
    completed: bool
    time: datetime
