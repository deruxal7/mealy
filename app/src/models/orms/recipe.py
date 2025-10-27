from sqlalchemy import (
    ARRAY,
    Column, 
    Integer,
    String,
)

from .base import BaseORM

class RecipeORM(BaseORM):
    __tablename__ = "recipe"

    recipe_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    ingredients = Column(ARRAY(String))
    instructions = Column(String)
    cooking_time = Column(Integer)
    tags = Column(ARRAY(String), default=[])
