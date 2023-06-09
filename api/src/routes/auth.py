from fastapi import APIRouter
from ..scemas import User

router = APIRouter()

@router.get("/api/login/",tags=['login'])
def login():
    return {"message": "user"}

@router.post("/api/logout/",tags=['login'])
def logout(user:User):
    return {"message": user}


