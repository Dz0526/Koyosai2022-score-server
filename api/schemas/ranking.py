from pydantic import BaseModel,Field
from typing import List

class RankingBase(BaseModel):
    id: int
    name: str = Field(None, example="伊藤大輝")
    rate: int
    rank: int
    
class Ranking(BaseModel):
    first: RankingBase
    self: RankingBase
    higher_around_rank_users: List[RankingBase]
    lower_around_rank_users: List[RankingBase]

    class Config:
        orm_mode = True
