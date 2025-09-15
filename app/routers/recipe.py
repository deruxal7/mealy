from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from ..schemas.recipe import RecipeOut, RecipeIn
from ..models.orms.base import get_db
from ..services import RecipeCRUD

router = APIRouter(prefix="/recipe", tags=["recipe"])

@router.post(
    "/",
    response_model = RecipeOut,
    responses = {
        200: {"description": "Success"},
        422: {"description": "Validation error"},
        500: {"description": "Internal server error"}
    }
)
async def create_recipe(payload: RecipeIn, db: AsyncSession = Depends(get_db)):
    """Create a new recipe"""
    data = payload.to_dict()
    new_recipe = await RecipeCRUD.create(db, data)
    return new_recipe

@router.get(
        "/recipes/", 
        response_model=List[RecipeOut]
)
async def read_recipes(db: AsyncSession = Depends(get_db)):
    response = await db.execute(select(RecipeCRUD.model))
    return response.scalars().all()

@router.get(
        "/recipes/{recipe_id}", 
        response_model=RecipeOut
)
async def read_recipe(recipe_id: int, db: AsyncSession = Depends(get_db)):
    recipe = await db.get(RecipeCRUD.model, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe