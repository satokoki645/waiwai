from fastapi import FastAPI
from src.routes import team,user,product,product_category,category

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

app.include_router(user.router)
app.include_router(team.router)
app.include_router(product.router)
app.include_router(product_category.router)
app.include_router(category.router)
