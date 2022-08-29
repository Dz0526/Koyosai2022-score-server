from imp import NullImporter
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(1024), nullable=False)


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer,primary_key=True)
    rate = Column(Float, nullable=False)

    user_id = Column(ForeignKey("users.id"), nullable=False)