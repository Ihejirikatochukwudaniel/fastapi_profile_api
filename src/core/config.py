import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    CAT_FACTS_API_URL: str = os.getenv("CAT_FACTS_API_URL", "https://catfact.ninja/fact")
    API_TIMEOUT: int = int(os.getenv("API_TIMEOUT", 5))

settings = Settings()
