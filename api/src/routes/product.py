from fastapi import APIRouter
from ..schemas import Product

router = APIRouter()

@router.get("/api/product",tags=['product'])
def get_product_all():
    return {"message": "product"}

@router.post("/api/product/",tags=['product'])
def create_product(product:Product):
    return {"message": product}

@router.put("/api/product/{id}",tags=['product'])
def update_product(product:Product):
    return {"message": product}

@router.delete("/api/product/{id}",tags=['product'])
def delete_product(product:Product):
    return {"message": product}