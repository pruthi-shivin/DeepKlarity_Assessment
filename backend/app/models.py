from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime
from .database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)

    url = Column(String, nullable=False)
    title = Column(String)
    cuisine = Column(String)

    prep_time = Column(String)
    cook_time = Column(String)
    total_time = Column(String)

    servings = Column(Integer)
    difficulty = Column(String)

    ingredients = Column(JSON)
    instructions = Column(JSON)

    nutrition_estimate = Column(JSON)
    substitutions = Column(JSON)
    shopping_list = Column(JSON)
    related_recipes = Column(JSON)

    raw_content = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)