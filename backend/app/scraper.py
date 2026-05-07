import requests
from bs4 import BeautifulSoup
import json


headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}


def extract_recipe_content(url: str):

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch URL: {response.status_code}"
        )

    soup = BeautifulSoup(response.text, "lxml")

    scripts = soup.find_all(
        "script",
        type="application/ld+json"
    )

    recipe_schema = None

    for script in scripts:

        try:

            if not script.string:
                continue

            data = json.loads(script.string)

            def find_recipe(obj):

                if isinstance(obj, dict):

                    obj_type = obj.get("@type")

                    if (
                        obj_type == "Recipe"
                        or (
                            isinstance(obj_type, list)
                            and "Recipe" in obj_type
                        )
                    ):
                        return obj

                    for value in obj.values():

                        result = find_recipe(value)

                        if result:
                            return result

                elif isinstance(obj, list):

                    for item in obj:

                        result = find_recipe(item)

                        if result:
                            return result

                return None

            recipe_schema = find_recipe(data)

            if recipe_schema:
                break

        except:
            continue

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    return {
        "raw_text": text[:4000],
        "html": response.text,
        "recipe_schema": recipe_schema
    }