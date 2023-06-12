from fastapi import FastAPI
from src.routes import user,team,product,product_category,category,auth
from models import Base
from database import engine

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(team.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(product_category.router)
app.include_router(category.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
