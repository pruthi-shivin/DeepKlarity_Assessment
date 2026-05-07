from sqlalchemy.orm import Session
from .models import Recipe


def create_recipe(db: Session, recipe_data: dict):
    recipe = Recipe(**recipe_data)

    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    return recipe


def get_all_recipes(db: Session):
    return db.query(Recipe).order_by(Recipe.created_at.desc()).all()


def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()