from click import echo
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://fastapi:fastapi@posgres/score-server"

engine = create_engine(DATABASE_URL, echo=True)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close
