# DeepKlarity Recipe Extractor

A full-stack AI-ready recipe extraction platform built using FastAPI, React, PostgreSQL, and web scraping techniques.

The application extracts recipe information dynamically from recipe websites, stores recipes in PostgreSQL, and provides a clean frontend interface for viewing recipe history and details.

---

# Features

## Recipe Extraction
- Extracts recipe data from recipe URLs
- Uses schema.org JSON-LD recipe scraping
- Dynamically parses:
  - Title
  - Ingredients
  - Instructions
  - Cuisine
  - Prep/Cook Time
  - Servings

## AI-Ready Enhancement Layer
- Dynamic nutrition estimation
- Ingredient substitution suggestions
- Related recipe recommendations
- Difficulty estimation

## Recipe History
- Stores extracted recipes in PostgreSQL
- View saved recipes
- Open detailed recipe modal

## Responsive Frontend
- Modern React UI
- Modal-based recipe details
- Responsive layout
- Clean user experience

---

# Tech Stack

## Frontend
- React
- Vite
- Axios
- CSS

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- BeautifulSoup
- Requests

## Database
- Neon PostgreSQL

---

# Project Structure

```txt
deepklarity-assignment/
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   ├── .env.example
│
├── frontend/
│   ├── src/
│   ├── package.json
│
├── prompts/
├── sample_data/
├── screenshots/
│
├── README.md
└── .gitignore

Setup Instructions

Backend Setup
1. Navigate to backend
    cd backend

2. Create virtual environment
    python -m venv venv

3. Activate environment

    -Windows
        venv\\Scripts\\activate
    -Mac/Linux
        source venv/bin/activate

4. Install dependencies
    pip install -r requirements.txt

5. Create a .env file inside backend folder.

    Example:
    DATABASE_URL=your_neon_database_url
    HF_API_KEY=your_huggingface_api_key


6. Run backend server
    uvicorn app.main:app --reload

Backend runs at:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs

_____________________________________________________________________

Frontend Setup

1. Navigate to frontend
    cd frontend

2. Install packages
    npm install

3. Run frontend
    npm run dev

Frontend runs at:

http://localhost:5173

_____________________________________________________________________

API Endpoints

Extract Recipe:

POST
/api/recipes/extract
Request Body
{
  "url": "https://example.com/recipe"
}

Get Recipe History:

GET
/api/recipes

Screenshots:
See:

screenshots/recipe-extraction-page_url+recipe-info.png
screenshots/recipe-extraction-page_url.png
screenshots/recipe-extraction-page_recipe-info.png
screenshots/history_page.png
screenshots/modal_popup.png


Sample Data:
Sample URLs and outputs are available inside:

sample_data/

Includes:

sample_data.txt
sample_output_1.json
sample_output_2.json
sample_output_3.json
sample_output_4.json


Prompt Templates:
Prompt templates are available inside:

prompts/

Includes:

recipe_extraction_prompt.txt
nutrition_prompt.txt
substitution_prompt.txt

Architecture Notes

The system uses a hybrid extraction pipeline:

Deterministic schema-based recipe extraction using JSON-LD parsing
Semantic enhancement layer for:
nutrition estimation
substitutions
related recipes
difficulty scoring

The architecture is modular and AI-provider agnostic, allowing future integration with:

Gemini
OpenAI
Groq
Local LLMs
Error Handling

The application handles:

Invalid URLs
Missing recipe schemas
Database errors
Extraction failures
Unsupported recipe pages
Future Improvements
Real LLM integration
OCR support for image recipes
Meal planning calendar
User authentication
Recipe bookmarking
Shopping cart integration
