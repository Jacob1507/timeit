from contextlib import asynccontextmanager

from fastapi import FastAPI
from .api.task import router as task_router

from .infrastructure.in_memory_db.config import Database



@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(title="TimeIT", lifespan=lifespan)

app.include_router(task_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)