from fastapi import APIRouter
from ..schemas import User

router = APIRouter()

@router.get("/api/user/",tags=['user'])
def get_user():
    return {"message": "user"}

@router.post("/api/user/",tags=['user'])
def create_user(user:User):
    return {"message": user}

@router.put("/api/user/{id}",tags=['user'])
def update_user(user:User):
    return {"message": user}

@router.delete("/api/user/{id}",tags=['user'])
def delete_user(user:User):
    return {"message": user}

