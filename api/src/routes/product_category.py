from fastapi import APIRouter
from ..scemas import product_category

router = APIRouter()

@router.get("/api/product_category/{id}",tags=['product_category'])
def get_product_category():
    return {"message": "product_category"}

@router.post("/api/product_category/",tags=['product_category'])
def create_product_category(product_category:product_category):
    return {"message": product_category}

@router.put("/api/product_category/{id}",tags=['product_category'])
def update_product_category(product_category:product_category):
    return {"message": product_category}

@router.delete("/api/product_category/{id}",tags=['product_category'])
def delete_product_category(product_category:product_category):
    return {"message": product_category}