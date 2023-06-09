from fastapi import APIRouter

router = APIRouter()

@router.get("/api/product")
def root():
    return {"message": "product"}