from typing import List
from pydantic import Field, PositiveInt

from .base import BaseModel

class RecipeIn(BaseModel):
    title: str = Field(..., description="Name of recipe")
    description: str = Field(..., description="Description of recipe")
    ingredients: List[str] = Field(..., description="List of ingredients")
    instructions: str = Field(..., description="Instruction to cook")
    cooking_time: PositiveInt = Field(..., description="Time to cook (min)")
    tags: List[str] = Field(..., description="Tags")

class RecipeOut(BaseModel):
    recipe_id: PositiveInt = Field(..., description="Recipe ID")
    title: str = Field(..., description="Name of recipe")
    description: str = Field(..., description="Description of recipe")
    ingredients: List[str] = Field(..., description="List of ingredients")
    instructions: str = Field(..., description="Instruction to cook")
    cooking_time: PositiveInt = Field(..., description="Time to cook (min)")
    tags: List[str] = Field(..., description="Tags")
    # author_id: PositiveInt = Field(..., description="Author ID")
