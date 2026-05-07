import { useEffect, useState } from "react";

import API from "./services/api";

import RecipeDetails from "./components/RecipeDetails";
import HistoryTable from "./components/HistoryTable";
import Modal from "./components/Modal";


function App() {

  const [activeTab, setActiveTab] = useState("extract");

  const [url, setUrl] = useState("");

  const [recipe, setRecipe] = useState(null);

  const [history, setHistory] = useState([]);

  const [loading, setLoading] = useState(false);

  const [selectedRecipe, setSelectedRecipe] = useState(null);


  const extractRecipe = async () => {

    if (!url) return;

    try {

      setLoading(true);

      const response = await API.post(
        "/recipes/extract",
        { url }
      );

      setRecipe(response.data);

      fetchHistory();

    } catch (error) {

      console.log(error);

      alert(
      error?.response?.data?.detail ||
      "Extraction failed"
    );

    } finally {

      setLoading(false);
    }
  };


  const fetchHistory = async () => {

    try {

      const response = await API.get(
        "/recipes"
      );

      setHistory(response.data);

    } catch (error) {

      console.log(error);
    }
  };


  useEffect(() => {

    fetchHistory();

  }, []);


  return (
    <div className="app">

      <h1 className="title">
        Recipe Extractor
      </h1>


      <div className="tabs">

        <button
          className={
            activeTab === "extract"
              ? "active"
              : ""
          }
          onClick={() => setActiveTab("extract")}
        >
          Extract Recipe
        </button>

        <button
          className={
            activeTab === "history"
              ? "active"
              : ""
          }
          onClick={() => setActiveTab("history")}
        >
          Saved Recipes
        </button>

      </div>


      {
        activeTab === "extract" && (

          <>
            <div className="input-section">

              <input
                type="text"
                placeholder="Enter recipe URL..."
                value={url}
                onChange={(e) => setUrl(e.target.value)}
              />

              <button onClick={extractRecipe}>
                {
                  loading
                    ? "Extracting..."
                    : "Extract Recipe"
                }
              </button>

            </div>

            {
              recipe && (
                <RecipeDetails recipe={recipe} />
              )
            }
          </>
        )
      }


      {
        activeTab === "history" && (

          <HistoryTable
            history={history}
            onView={(recipe) =>
              setSelectedRecipe(recipe)
            }
          />
        )
      }


      {
        selectedRecipe && (

          <Modal
            onClose={() =>
              setSelectedRecipe(null)
            }
          >
            <RecipeDetails
              recipe={selectedRecipe}
            />
          </Modal>
        )
      }

    </div>
  );
}

export default App;