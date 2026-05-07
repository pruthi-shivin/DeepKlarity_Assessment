function RecipeDetails({ recipe }) {

  return (

    <div className="card">

      <div className="recipe-header">

        <h2 className="recipe-title">
          {recipe.title}
        </h2>

        <div className="recipe-badge">
          {recipe.difficulty}
        </div>

      </div>


      <div className="recipe-info">

        <div className="info-box">
          <h4>Cuisine</h4>
          <p>{recipe.cuisine}</p>
        </div>

        <div className="info-box">
          <h4>Prep Time</h4>
          <p>{recipe.prep_time}</p>
        </div>

        <div className="info-box">
          <h4>Cook Time</h4>
          <p>{recipe.cook_time}</p>
        </div>

        <div className="info-box">
          <h4>Total Time</h4>
          <p>{recipe.total_time}</p>
        </div>

      </div>


      <div className="grid-sections">

        <div className="section-card">

          <h3 className="section-title">
            Ingredients
          </h3>

          <ul className="list">

            {
              recipe.ingredients?.map(
                (ingredient, index) => (

                  <li key={index}>
                    {ingredient.quantity}{" "}
                    {ingredient.unit}{" "}
                    {ingredient.item}
                  </li>
                )
              )
            }

          </ul>

        </div>


        <div className="section-card">

          <h3 className="section-title">
            Instructions
          </h3>

          <ol className="list">

            {
              recipe.instructions?.map(
                (step, index) => (

                  <li key={index}>
                    {step}
                  </li>
                )
              )
            }

          </ol>

        </div>


        <div className="section-card">

          <h3 className="section-title">
            Nutrition
          </h3>

          <p>
            <strong>Calories:</strong>{" "}
            {recipe.nutrition_estimate?.calories}
          </p>

          <p>
            <strong>Protein:</strong>{" "}
            {recipe.nutrition_estimate?.protein}
          </p>

          <p>
            <strong>Carbs:</strong>{" "}
            {recipe.nutrition_estimate?.carbs}
          </p>

          <p>
            <strong>Fat:</strong>{" "}
            {recipe.nutrition_estimate?.fat}
          </p>

        </div>


        <div className="section-card">

          <h3 className="section-title">
            Substitutions
          </h3>

          <ul className="list">

            {
              recipe.substitutions?.map(
                (item, index) => (

                  <li key={index}>
                    {item}
                  </li>
                )
              )
            }

          </ul>

        </div>


        <div className="section-card">

          <h3 className="section-title">
            Related Recipes
          </h3>

          <ul className="list">

            {
              recipe.related_recipes?.map(
                (item, index) => (

                  <li key={index}>
                    {item}
                  </li>
                )
              )
            }

          </ul>

        </div>

      </div>

    </div>
  );
}

export default RecipeDetails;