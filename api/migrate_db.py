from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import  Team
from models import Base

DB_URL = "postgresql://user:password@host.docker.internal:5432/waiwai_db"
engine = create_engine(DB_URL, echo=True)

Session = sessionmaker(bind=engine)  # engineをバインドしてSessionを作成
session = Session()

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


    session = Session()

    team1 = Team(id=0,team_name="test0")
    session.add(team1)
    session.commit()


if __name__ == "__main__":
    reset_database()
