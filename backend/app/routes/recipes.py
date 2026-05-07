from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Recipe
from ..schemas import RecipeURL
from ..scraper import scrape_recipe
from ..llm_service import generate_recipe_data


router = APIRouter(
    prefix="/api/recipes",
    tags=["Recipes"]
)


@router.post("/extract")
def extract_recipe(recipe_input: RecipeURL):

    try:

        recipe_schema = scrape_recipe(
            recipe_input.url
        )

        generated_recipe = generate_recipe_data(
            recipe_schema
        )

        db: Session = SessionLocal()

        new_recipe = Recipe(
            title=generated_recipe["title"],
            cuisine=generated_recipe["cuisine"],
            prep_time=generated_recipe["prep_time"],
            cook_time=generated_recipe["cook_time"],
            total_time=generated_recipe["total_time"],
            servings=generated_recipe["servings"],
            difficulty=generated_recipe["difficulty"],
            ingredients=generated_recipe["ingredients"],
            instructions=generated_recipe["instructions"],
            nutrition_estimate=generated_recipe["nutrition_estimate"],
            substitutions=generated_recipe["substitutions"],
            shopping_list=generated_recipe["shopping_list"],
            related_recipes=generated_recipe["related_recipes"]
        )

        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)

        return new_recipe

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("")
def get_recipes():

    db: Session = SessionLocal()

    recipes = db.query(
        Recipe
    ).order_by(
        Recipe.created_at.desc()
    ).all()

    return recipes