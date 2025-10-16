FastAPI Profile API — README

Clear, practical guide that documents the project, explains design choices, and gives step-by-step instructions to run the /me endpoint locally.

Project summary

This FastAPI project provides a single GET endpoint at /me that returns a JSON payload with:

status: the string "success"

user: your profile object with email, name, and stack

timestamp: current UTC time in ISO 8601 format with trailing Z (example: 2025-10-16T12:34:56.789Z)

fact: a random cat fact fetched live from the Cat Facts API (https://catfact.ninja/fact)

Design goals:

Simple, testable, and well structured

Uses async HTTP client (httpx.AsyncClient) to fetch external data

Graceful fallback if external API fails

Environment driven configuration via .env

Windows-friendly notes and troubleshooting included

Folder structure
fastapi_profile_api/
│
├── src/
│   ├── main.py                # FastAPI app and route registration
│   ├── api/
│   │   └── routes_me.py       # /me route implementation
│   ├── core/
│   │   ├── config.py          # settings and timeouts
│   │   └── utils.py           # timestamp helper
│   ├── services/
│   │   └── cat_facts.py       # Cat Facts API integration (async)
│   └── tests/
│       └── test_me_endpoint.py
│
├── venv/                      # virtual environment (created locally)
├── .env                       # runtime env vars (optional)
├── README.md
├── requirements.txt
└── run.py                     # launcher (uvicorn)

Prerequisites

Python 3.11 or 3.12 installed and available in PATH

Git (optional)

On Windows use PowerShell or Command Prompt

Internet connection (to fetch cat facts)

Quick start — copy/paste sequence (Windows PowerShell)

open PowerShell and change to project directory:

cd C:\Users\USER\Documents\fastapi_profile_api


create virtual environment:

python -m venv venv


activate venv:

venv\Scripts\Activate.ps1
# if you use cmd.exe instead:
# venv\Scripts\activate


install core dependencies:

pip install -r requirements.txt


(optional) install httpx and python-dotenv separately if you prefer them managed manually:

pip install httpx
pip install python-dotenv
# verify
pip show httpx
pip show python-dotenv
# record dependencies
pip freeze > requirements.txt


set environment variables (optional). Create or edit .env in project root:

CAT_FACTS_API_URL=https://catfact.ninja/fact
API_TIMEOUT=5


run the app with reload enabled (recommended for development):

python run.py


open the API in the browser:

Root: http://127.0.0.1:8000/

Endpoint: http://127.0.0.1:8000/me

Note: do not use http://0.0.0.0:8000/ in the browser. Use 127.0.0.1 or localhost.

How the code works (quick walkthrough)

src/main.py creates FastAPI() as app, registers CORS middleware, and includes the route router from src/api/routes_me.py.

src/api/routes_me.py defines the /me endpoint as an async function. It awaits fetch_cat_fact() and builds the response exactly in the required schema.

src/services/cat_facts.py uses httpx.AsyncClient with a timeout from settings to fetch CAT_FACTS_API_URL. On error it returns a fallback message string so the /me endpoint still returns status: "success".

src/core/config.py centralizes configuration variables and reads .env if present.

src/core/utils.py provides get_current_utc_time() which returns UTC ISO 8601 with milliseconds and Z.

Example /me response
{
  "status": "success",
  "user": {
    "email": "ihejirikatochukwu@gmail.com",
    "name": "Ihejirika Tochukwu Daniel",
    "stack": "FastAPI"
  },
  "timestamp": "2025-10-16T12:34:56.789Z",
  "fact": "Cats have five toes on their front paws, but only four on the back."
}

Running tests

If you included the tests folder, run unit tests with pytest. First install pytest:

pip install pytest


Then run:

pytest -q

Common problems and fixes

ERROR: Error loading ASGI app. Attribute "app" not found in module "src.main".

Ensure src/main.py contains app = FastAPI(...).

Confirm you run from the project root (the folder that contains src/).

Confirm src/__init__.py exists (empty file is fine).

ImportError: cannot import name 'router' from 'src.api.routes_me'

Ensure routes_me.py defines router = APIRouter() and exports it.

If your route is async, define async def functions and await service calls.

ModuleNotFoundError: No module named 'app' after renaming app to src

Update imports inside service modules to use src, e.g. from src.core.config import settings.

ImportError: cannot import name 'app' when using direct import in run.py

If you want reload mode, uvicorn needs an import string. Use:

uvicorn.run("src.main:app", reload=True)


If you import app directly, use uvicorn.run(app, reload=False) or remove reload=True.

ERR_ADDRESS_INVALID in browser when opening http://0.0.0.0:8000/

Use http://127.0.0.1:8000/ or http://localhost:8000/

Notes for development and deployment

For development, reload=True is extremely helpful. Uvicorn requires the import string form to enable reload:

uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)


For production, use a proper ASGI server configuration and workers and set reload=False.

Consider rate limiting and caching for production scenarios.

Put sensitive values like API keys into environment variables, not in repository.

Environment variables reference

CAT_FACTS_API_URL — URL for cat facts (defaults to https://catfact.ninja/fact)

API_TIMEOUT — request timeout in seconds (defaults to 5)

Extra tips

If you prefer using pipenv or poetry the same steps apply for creating an isolated environment.

When you change package imports or rename top-level package folder, check all import statements and update them to the new package name. Python import errors seen during startup usually mean an incorrect import path.

To capture logs from the cat facts fetch, add logging inside src/services/cat_facts.py and routes_me.py.
