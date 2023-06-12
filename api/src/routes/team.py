from fastapi import APIRouter
from ..schemas import Team

router = APIRouter()

@router.get("/api/teams",tags=['teams'])
def get_team_all():
    return {"message": "team"}

@router.post("/api/teams/",tags=['teams'])
def create_team(team:Team):
    return {"message": team}

@router.put("/api/teams/{id}",tags=['teams'])
def update_team(team:Team):
    return {"message": team}

@router.delete("/api/teams/{id}",tags=['teams'])
def delete_team(team:Team):
    return {"message": team}