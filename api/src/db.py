from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://user:password@postgresql:5432/postgres"

async_engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

BaseModel = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session