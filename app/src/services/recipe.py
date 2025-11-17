from .base import BaseCRUD, with_model
from ..models.orms import RecipeORM

@with_model(RecipeORM)
class RecipeCRUD(BaseCRUD):
    model = RecipeORM