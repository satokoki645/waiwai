from fastapi import APIRouter

router = APIRouter()

@router.get("/api/category")
def root():
    return {"message": "category"}