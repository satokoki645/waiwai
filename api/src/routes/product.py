from fastapi import APIRouter
from src.schemas.schemas import Product
from sqlalchemy.orm import Session
import models
from database import get_db

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