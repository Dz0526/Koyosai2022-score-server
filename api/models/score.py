from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.database import Base


class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer,primary_key=True)
    rate = Column(Float,nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)
