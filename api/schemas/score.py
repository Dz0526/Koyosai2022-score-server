from pydantic import BaseModel

class ScoreBase(BaseModel):
    
    rate: int
    
class ScoreCreate(ScoreBase):
    pass

class Score(ScoreBase):
    
    id: int

class ScoreCreateResponse(ScoreBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
