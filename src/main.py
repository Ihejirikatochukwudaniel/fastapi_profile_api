from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes_me import router as me_router

app = FastAPI(
    title="Profile API",
    version="1.0.0",
    description="Dynamic /me endpoint with Cat Facts integration."
)

# Optional CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(me_router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Profile API. Visit /me to see your profile info."}
