from fastapi import APIRouter,Depends,status
from src.schemas.schemas import Team,ShowTeam
from sqlalchemy.orm import Session
import models
from database import get_db

router = APIRouter()

@router.get("/api/teams",status_code=status.HTTP_200_OK,tags=['teams'])
def get_team_all(db:Session=Depends(get_db)):
    new_team = db.query(models.Team).all()
    return new_team

@router.post("/api/teams/",status_code=status.HTTP_201_CREATED,tags=['teams'])
def create_team(team:Team,db:Session=Depends(get_db)):
    new_team = models.Team(id =team.id,team_name =team.team_name)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return  new_team

@router.put("/api/teams/{id}",status_code=status.HTTP_202_ACCEPTED,tags=['teams'])
def update_team(id:int,request:ShowTeam,db:Session=Depends(get_db)):
    db.query(models.Team).filter(models.Team.id ==id).update(request.dict())
    db.commit()
    return 'Update complete'

@router.delete("/api/teams/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=['teams'])
def delete_team(id:int,db:Session=Depends(get_db)):
    db.query(models.Team).filter(models.Team.id ==id).delete(synchronize_session=False)
    db.commit()
    return "Deletion competed"