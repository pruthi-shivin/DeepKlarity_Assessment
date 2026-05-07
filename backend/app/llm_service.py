def generate_recipe_data(recipe_schema):

    if not recipe_schema:

        return {
            "title": "Recipe Extracted",
            "cuisine": "Unknown",
            "prep_time": "",
            "cook_time": "",
            "total_time": "",
            "servings": 2,
            "difficulty": "medium",
            "ingredients": [],
            "instructions": [
                "Recipe schema not available for this website."
            ],
            "nutrition_estimate": {
                "calories": "",
                "protein": "",
                "carbs": "",
                "fat": ""
            },
            "substitutions": [],
            "shopping_list": {},
            "related_recipes": []
        }

    ingredients = []

    raw_ingredients = recipe_schema.get(
        "recipeIngredient",
        []
    )

    for ingredient in raw_ingredients:

        ingredients.append({
            "quantity": "",
            "unit": "",
            "item": ingredient
        })

    instructions = []

    raw_instructions = recipe_schema.get(
        "recipeInstructions",
        []
    )

    for step in raw_instructions:

        if isinstance(step, dict):

            instructions.append(
                step.get("text", "")
            )

        else:

            instructions.append(str(step))

    ingredient_text = " ".join(
        raw_ingredients
    ).lower()

    substitutions = []

    if "butter" in ingredient_text:
        substitutions.append(
            "Use olive oil instead of butter"
        )

    if "sugar" in ingredient_text:
        substitutions.append(
            "Replace sugar with honey"
        )

    if "milk" in ingredient_text:
        substitutions.append(
            "Use almond milk instead of regular milk"
        )

    if "cream" in ingredient_text:
        substitutions.append(
            "Use greek yogurt instead of cream"
        )

    if "flour" in ingredient_text:
        substitutions.append(
            "Use oat flour instead of all-purpose flour"
        )

    if not substitutions:
        substitutions = [
            "Use healthier ingredient alternatives if needed"
        ]


    related_recipes = []

    title = recipe_schema.get(
        "name",
        ""
    ).lower()

    if "chicken" in title:
        related_recipes = [
            "Garlic Chicken",
            "Chicken Curry",
            "Chicken Alfredo"
        ]

    elif "pasta" in title:
        related_recipes = [
            "White Sauce Pasta",
            "Arrabbiata Pasta",
            "Mac and Cheese"
        ]

    elif "cake" in title:
        related_recipes = [
            "Chocolate Cake",
            "Vanilla Cupcakes",
            "Brownies"
        ]

    elif "sandwich" in title:
        related_recipes = [
            "Club Sandwich",
            "Veg Sandwich",
            "Cheese Toast"
        ]

    else:
        related_recipes = [
            "Recipe A",
            "Recipe B",
            "Recipe C"
        ]


    calories = "300"
    protein = "10g"
    carbs = "20g"
    fat = "15g"

    ingredient_count = len(raw_ingredients)

    if ingredient_count > 10:
        calories = "550"
        protein = "22g"
        carbs = "45g"
        fat = "28g"

    elif ingredient_count > 5:
        calories = "420"
        protein = "16g"
        carbs = "32g"
        fat = "20g"


    difficulty = "easy"

    if len(instructions) > 8:
        difficulty = "hard"

    elif len(instructions) > 4:
        difficulty = "medium"


    shopping_list = {
        "general": raw_ingredients
    }


    return {

        "title": recipe_schema.get(
            "name",
            ""
        ),

        "cuisine": recipe_schema.get(
            "recipeCuisine",
            "International"
        ),

        "prep_time": recipe_schema.get(
            "prepTime",
            ""
        ),

        "cook_time": recipe_schema.get(
            "cookTime",
            ""
        ),

        "total_time": recipe_schema.get(
            "totalTime",
            ""
        ),

        "servings": recipe_schema.get(
            "recipeYield",
            2
        ),

        "difficulty": difficulty,

        "ingredients": ingredients,

        "instructions": instructions,

        "nutrition_estimate": {
            "calories": calories,
            "protein": protein,
            "carbs": carbs,
            "fat": fat
        },

        "substitutions": substitutions,

        "shopping_list": shopping_list,

        "related_recipes": related_recipes
    }