from fastapi import APIRouter

router = APIRouter()

@router.get("/api/product_category")
def root():
    return {"message": "product_category"}