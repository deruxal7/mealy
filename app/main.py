from fastapi import FastAPI

from .config import settings
from .models.orms.base import create_tables
from .routers.recipe import router as recipe_router
from .routers.base import router as base_router

app = FastAPI(title = "Mealie",
              description = "My education project for view recipes",
              docs_url = f"{settings.API_BASE_URL}/swagger"
)

@app.on_event("startup")
async def on_startup():
    await create_tables()

app.include_router(recipe_router, prefix=settings.API_BASE_URL)
app.include_router(base_router, prefix=settings.API_BASE_URL)