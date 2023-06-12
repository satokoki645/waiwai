from fastapi import APIRouter,Depends
from ..schemas import Team,ShowTeam
from sqlalchemy.orm import Session
import models
from database import get_db

router = APIRouter()

@router.get("/api/teams",tags=['teams'])
def get_team_all(db:Session=Depends(get_db)):
    new_team = db.query(models.Team).all()
    return new_team

@router.post("/api/teams/",tags=['teams'])
def create_team(team:Team,db:Session=Depends(get_db)):
    new_team = models.Team(id =team.id,team_name =team.team_name)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return  new_team

@router.put("/api/teams/{id}",tags=['teams'])
def update_team(id:int,request:ShowTeam,db:Session=Depends(get_db)):
    db.query(models.Team).filter(models.Team.id ==id).update(request.dict())
    db.commit()
    return 'Update complete'

@router.delete("/api/teams/{id}",tags=['teams'])
def delete_team(id:int,db:Session=Depends(get_db)):
    db.query(models.Team).filter(models.Team.id ==id).delete(synchronize_session=False)
    db.commit()
    return "Deletion competed"