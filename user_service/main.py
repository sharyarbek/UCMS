from contextlib import asynccontextmanager

from fastapi import FastAPI

from user_service.routes import router as user_router
from database import setup_database

@asynccontextmanager
async def lifespan(main_app: FastAPI):
    await setup_database()

    yield



app = FastAPI(
    title="University Course Management System",
    version="0.1",
    summary="Programming CourseWork",
    lifespan=lifespan,
)


app.include_router(user_router, prefix='/user', tags=['User'])