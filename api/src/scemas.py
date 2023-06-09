from pydantic import BaseModel
from typing import List,Optional

class User(BaseModel):
    id :int
    user:str
    user_name:str
    password:str

class Team(BaseModel):
    id :int
    user_id:int
    team_name:str

class Product(BaseModel):
    id :int
    team_id:int
    category_id:int
    product_name:str
    quantity:int
    created_at:str
    updated_at:str

class category(BaseModel):
    category_id :int
    category_name:str
    category_color:str

class product_category(BaseModel):
    product_category_id :int
    product_id:int
    category_id:str