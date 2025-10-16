from fastapi import APIRouter
from src.services.cat_facts import fetch_cat_fact

router = APIRouter()

@router.get("/me")
async def get_me():
    cat_fact = await fetch_cat_fact()
    return {
        "status": "success",
        "user": {
            "name": "Tochukwu Ihejirika",
            "email": "tochukwuihejirika3@gmail.com",
            "stack": "Python / FastAPI",
        },
        "fact": cat_fact
    }
