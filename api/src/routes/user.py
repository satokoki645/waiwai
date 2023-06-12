from fastapi import APIRouter,Depends,Response
from ..schemas import User,ShowUser
from sqlalchemy.orm import Session
import models
from database import get_db


router = APIRouter()

@router.get("/api/user/{id}",tags=['user'])
def get_user(id:int,response:Response,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id ==id).first()
    return user

@router.post("/api/user/",tags=['user'])
def create_user(user:User,db:Session=Depends(get_db)):
    new_user = models.User(id=user.id,team_id=user.team_id,user_name=user.user_name,password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put("/api/user/{id}",tags=['user'])
def update_user(id,request:ShowUser,db:Session=Depends(get_db)):
    db.query(models.User).filter(models.User.id ==id).update(request.dict())
    db.commit()
    return 'Update complete'

@router.delete("/api/user/{id}",tags=['user'])
def delete_user(id:int,db:Session=Depends(get_db)):
    db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    return "Deletion competed"
