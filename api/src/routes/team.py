from fastapi import APIRouter

router = APIRouter()

@router.get("/api/teams")
def root():
    return {"message": "team"}