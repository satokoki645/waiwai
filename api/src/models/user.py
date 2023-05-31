from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    team_id = 