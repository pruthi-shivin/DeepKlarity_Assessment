from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime


class RecipeURL(BaseModel):
    url: str


class Ingredient(BaseModel):
    quantity: str
    unit: str
    item: str


class RecipeResponse(BaseModel):
    id: int
    url: str
    title: str
    cuisine: str

    prep_time: str
    cook_time: str
    total_time: str

    servings: int
    difficulty: str

    ingredients: List[Dict[str, Any]]
    instructions: List[str]

    nutrition_estimate: Dict[str, Any]
    substitutions: List[str]
    shopping_list: Dict[str, Any]
    related_recipes: List[str]

    created_at: datetime

    class Config:
        from_attributes = True