import pytest
from sqlalchemy import select

from src.models.orms.recipe import RecipeORM
from src.schemas.recipe import RecipeIn

@pytest.mark.asyncio
async def test_create_recipe(test_session):
    """Test creating a single recipe."""
    # Create recipe data
    recipe_data = RecipeIn(
        title="Test Recipe",
        description="A test recipe description",
        ingredients=["ingredient1", "ingredient2"],
        instructions="steps",
        cooking_time=25,
        tags=["test", "easy"]
    )
    
    # Create recipe in DB
    recipe = RecipeORM(
        title=recipe_data.title,
        description=recipe_data.description,
        ingredients=recipe_data.ingredients,
        instructions=recipe_data.instructions,
        cooking_time=recipe_data.cooking_time,
        tags=recipe_data.tags
    )
    test_session.add(recipe)
    await test_session.flush()
    
    # Verify recipe was created
    stmt = select(RecipeORM).where(RecipeORM.title == "Test Recipe")
    result = await test_session.execute(stmt)
    db_recipe = result.scalar_one()
    
    assert db_recipe.title == recipe_data.title
    assert db_recipe.description == recipe_data.description
    assert db_recipe.ingredients == recipe_data.ingredients
    assert db_recipe.instructions == recipe_data.instructions
    assert db_recipe.cooking_time == recipe_data.cooking_time
    assert db_recipe.tags == recipe_data.tags

# @pytest.mark.asyncio
# async def test_read_recipe(test_session):
#     """Test reading a recipe."""
#     # Create test recipe
#     recipe = RecipeORM(
#         title="Recipe to Read",
#         description="Description to read",
#         ingredients=["ing1", "ing2"],
#         instructions="1. First step\n2. Second step",
#         cooking_time=30,
#         tags=["test"]
#     )
#     test_session.add(recipe)
#     await test_session.commit()
    
#     # Read recipe
#     stmt = select(RecipeORM).where(RecipeORM.title == "Recipe to Read")
#     result = await test_session.execute(stmt)
#     db_recipe = result.scalar_one()
    
#     # Verify data
#     assert db_recipe.title == "Recipe to Read"
#     assert db_recipe.description == "Description to read"
#     assert db_recipe.ingredients == ["ing1", "ing2"]
#     assert db_recipe.instructions == "1. First step\n2. Second step"
#     assert db_recipe.cooking_time == 30
#     assert db_recipe.tags == ["test"]

# @pytest.mark.asyncio
# async def test_delete_recipe(test_session):
#     """Test deleting a recipe."""
#     # Create test recipe
#     recipe = RecipeORM(
#         title="Recipe to Delete",
#         description="Will be deleted",
#         ingredients=["ing1"],
#         instructions="Delete me",
#         cooking_time=15,
#         tags=["temp"]
#     )
#     test_session.add(recipe)
#     await test_session.commit()
    
#     # Delete recipe
#     stmt = select(RecipeORM).where(RecipeORM.title == "Recipe to Delete")
#     result = await test_session.execute(stmt)
#     db_recipe = result.scalar_one()
#     await test_session.delete(db_recipe)
#     await test_session.commit()
    
#     # Verify recipe was deleted
#     stmt = select(RecipeORM).where(RecipeORM.title == "Recipe to Delete")
#     result = await test_session.execute(stmt)
#     deleted_recipe = result.scalar_one_or_none()
#     assert deleted_recipe is None

# @pytest.mark.asyncio
# async def test_create_multiple_recipes(test_session):
#     """Test creating multiple recipes."""
#     recipes_data = [
#         {
#             "title": "Recipe 1",
#             "description": "First recipe",
#             "ingredients": ["ing1", "ing2"],
#             "instructions": "1. Step one\n2. Step two",
#             "cooking_time": 20,
#             "tags": ["easy"]
#         },
#         {
#             "title": "Recipe 2",
#             "description": "Second recipe",
#             "ingredients": ["ing3", "ing4"],
#             "instructions": "1. Step three\n2. Step four",
#             "cooking_time": 40,
#             "tags": ["medium"]
#         }
#     ]
    
#     # Create recipes
#     for recipe_data in recipes_data:
#         recipe = RecipeORM(**recipe_data)
#         test_session.add(recipe)
#     await test_session.commit()
    
#     # Verify all recipes were created
#     stmt = select(RecipeORM).order_by(RecipeORM.title)
#     result = await test_session.execute(stmt)
#     db_recipes = result.scalars().all()
    
#     assert len(db_recipes) == 2
#     assert db_recipes[0].title == "Recipe 1"
#     assert db_recipes[1].title == "Recipe 2"