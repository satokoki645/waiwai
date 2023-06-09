from fastapi import APIRouter
from ..scemas import category

router = APIRouter()

@router.get("/api/category/{id}",tags=['category'])
def get_category():
    return {"message": "category"}

@router.post("/api/category/",tags=['category'])
def create_category(category:category):
    return {"message": category}

@router.put("/api/category/{id}",tags=['category'])
def update_category(category:category):
    return {"message": category}

@router.delete("/api/category/{id}",tags=['category'])
def delete_category(category:category):
    return {"message": category}