from fastapi import APIRouter,Depends,status,HTTPException
from src.schemas.schemas import Team,CreateTeam
from sqlalchemy.orm import Session
import models
from database import get_db

def create_team(request:Team,db:Session):
    new_team = models.Team(team_name =request.team_name)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team

def show_team(db:Session):
    teams = db.query(models.Team).all()
    return teams

def delete_team(id:int,db:Session):
    team = db.query(models.Team).filter(models.Team.id ==id)
    if not team.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id} Blog with the is not found')
    team.delete(synchronize_session=False)
    db.commit()
    return 'Deletion competed'

def update_team(id:int,request:Team,db:Session):
    teams = db.query(models.Team).filter(models.Team.id ==id).update(request.dict())
    db.commit()
    return 'Deletion competed'