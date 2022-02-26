# Standard library imports
from typing import Dict

# Third party imports
import requests
from fastapi import FastAPI, Query
from mangum import Mangum

# Local application imports
from settings import AppConfig  # type: ignore

app = FastAPI(
    title=AppConfig.NAME,
)


@app.get("/anime/")
def search(q: str = Query(None, min_length=1, max_length=50)) -> Dict:

    response = requests.get("https://api.jikan.moe/v4/anime", params=[("q", q)])
    if response.ok:
        return {
            "count": len(response.json()["data"]),
            "results": [
                {
                    "title": record["title"],
                    "url": record["url"],
                }
                for record in response.json()["data"]
            ],
        }
    else:
        return {"count": 0, "results": []}


handler = Mangum(app)
