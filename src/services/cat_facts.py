import httpx
from src.core.config import settings

async def fetch_cat_fact() -> str:
    """
    Fetches a random cat fact from the Cat Facts API.
    Returns a fallback message if the request fails.
    """
    try:
        async with httpx.AsyncClient(timeout=settings.API_TIMEOUT) as client:
            response = await client.get(settings.CAT_FACTS_API_URL)
            response.raise_for_status()
            data = response.json()
            return data.get("fact", "No fact available.")
    except Exception:
        return "Could not fetch cat fact at this time."
