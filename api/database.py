from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session,sessionmaker


DATEBASE_URL = "postgresql://user:password@host.docker.internal:5432/waiwai_db"


engine = create_engine(DATEBASE_URL)

sessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base =declarative_base()

def get_db() -> Session:

    try:
        db =sessionLocal()
        yield db
    finally:
        db.close()
