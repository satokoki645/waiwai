from fastapi import APIRouter

router = APIRouter()

@router.get("/api/user/")
def root():
    return {"message": "user"}