from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routes.recipes import router as recipe_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DeepKlarity Recipe Extractor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipe_router)


@app.get("/")
def root():
    return {"message": "Recipe Extractor API Running"}