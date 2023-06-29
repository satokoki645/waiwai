from fastapi import APIRouter
from src.schemas.schemas import User

router = APIRouter()

@router.put("/api/login/",tags=['login'])
def login():
    return {"message": "user"}

@router.delete("/api/logout/",tags=['login'])
def logout(user:User):
    return {"message": user}


