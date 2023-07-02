from fastapi import APIRouter,Depends,status
from src.schemas.schemas import Team,CreateTeam
from sqlalchemy.orm import Session
import models
from database import get_db
from src.cruds import teams

router = APIRouter()

@router.get("/api/teams",status_code=status.HTTP_200_OK,tags=['teams'])
def get_team_all(db:Session=Depends(get_db)):
    return teams.show_team(db)

@router.post("/api/teams/",status_code=status.HTTP_201_CREATED,tags=['teams'])
def create_team(request:CreateTeam,db:Session=Depends(get_db)):
    return teams.create_team(request,db)

@router.put("/api/teams/{id}",status_code=status.HTTP_202_ACCEPTED,tags=['teams'])
def update_team(id:int,request:CreateTeam,db:Session=Depends(get_db)):
    return teams.update_team(id,request,db)

@router.delete("/api/teams/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=['teams'])
def delete_team(id:int,db:Session=Depends(get_db)):
    return teams.delete_team(id,db)