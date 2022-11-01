from click import echo
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

PGDATABASE=os.getenv('PGDATABASE')
PGHOST=os.getenv('PGHOST')
PGPASSWORD=os.getenv('PGPASSWORD')
PGPORT=os.getenv('PGPORT')
PGUSER=os.getenv('PGUSER')

DATABASE_URL = f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"

engine = create_engine(DATABASE_URL, echo=True)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close
