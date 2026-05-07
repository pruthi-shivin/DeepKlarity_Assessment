function HistoryTable({
  history,
  onView
}) {

  return (

    <table className="table">

      <thead>

        <tr>
          <th>Title</th>
          <th>Cuisine</th>
          <th>Difficulty</th>
          <th>Date</th>
          <th>Action</th>
        </tr>

      </thead>

      <tbody>

        {
          history.map((recipe) => (

            <tr key={recipe.id}>

              <td>
                {recipe.title}
              </td>

              <td>
                {recipe.cuisine}
              </td>

              <td>
                {recipe.difficulty}
              </td>

              <td>
                {
                  new Date(
                    recipe.created_at
                  ).toLocaleString()
                }
              </td>

              <td>

                <button
                className="details-btn"
                onClick={() =>
                    onView(recipe)
                }
                >
                Details
                </button>

              </td>

            </tr>
          ))
        }

      </tbody>

    </table>
  );
}

export default HistoryTable;