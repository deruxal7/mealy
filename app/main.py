from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.config import settings
from src.models.orms.base import create_tables
from src.routers.recipe import router as recipe_router
from src.routers.base import router as base_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(
    title = "Mealie",
    description = "My education project for view recipes",
    docs_url = f"{settings.api_base_url}/swagger",
    lifespan=lifespan,
)

app.include_router(recipe_router, prefix=settings.api_base_url)
app.include_router(base_router, prefix=settings.api_base_url)