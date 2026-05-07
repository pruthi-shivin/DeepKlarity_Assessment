from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import RecipeURLRequest
from ..scraper import extract_recipe_content
from ..llm_service import generate_recipe_data
from ..crud import create_recipe, get_all_recipes, get_recipe_by_id


router = APIRouter(
    prefix="/api/recipes",
    tags=["Recipes"]
)


@router.post("/extract")
def extract_recipe(
    request: RecipeURLRequest,
    db: Session = Depends(get_db)
):

    try:

        scraped_data = extract_recipe_content(request.url)

        generated_recipe = generate_recipe_data(
            scraped_data["recipe_schema"]
        )

        generated_recipe["url"] = request.url
        generated_recipe["raw_content"] = scraped_data["raw_text"]

        saved_recipe = create_recipe(
            db,
            generated_recipe
        )

        return saved_recipe

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/")
def get_recipes(db: Session = Depends(get_db)):
    return get_all_recipes(db)


@router.get("/{recipe_id}")
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):

    recipe = get_recipe_by_id(db, recipe_id)

    if not recipe:
        raise HTTPException(
            status_code=404,
            detail="Recipe not found"
        )

    return recipe