import requests
from bs4 import BeautifulSoup
import json


def scrape_recipe(url):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": (
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,image/webp,*/*;q=0.8"
        ),
        "Connection": "keep-alive"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    if response.status_code != 200:

        raise Exception(
            f"Failed to fetch URL: {response.status_code}"
        )

    soup = BeautifulSoup(
        response.text,
        "lxml"
    )

    scripts = soup.find_all(
        "script",
        type="application/ld+json"
    )

    for script in scripts:

        try:

            if not script.string:
                continue

            data = json.loads(
                script.string
            )

            if isinstance(data, list):

                for item in data:

                    if (
                        isinstance(item, dict)
                        and item.get("@type") == "Recipe"
                    ):

                        return item

            elif isinstance(data, dict):

                if data.get("@type") == "Recipe":

                    return data

                if "@graph" in data:

                    for item in data["@graph"]:

                        if (
                            isinstance(item, dict)
                            and item.get("@type") == "Recipe"
                        ):

                            return item

        except Exception:
            continue

    raise Exception(
        "No recipe schema found"
    )