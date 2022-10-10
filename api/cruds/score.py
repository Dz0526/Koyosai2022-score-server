from sqlalchemy.ext.asyncio import AsyncSession

import api.models.user as user_model
import api.models.score as score_model
import api.schemas.score as score_schema

from typing import List, Tuple, Optional
from sqlalchemy import select,desc,func
from sqlalchemy.engine import Result
import logging

async def get_user_score(db:AsyncSession, user_id: int) -> List[Tuple[int, int]]:

    result: Result = (
        db.execute(
            select(
                score_model.Score.id,
                score_model.Score.rate,
            ).filter(score_model.Score.user_id == user_id)
        )
    )
    return result.all()

async def create_user_score(
    db: AsyncSession, score_create: score_schema.ScoreCreate, user_id: int
) -> score_model.Score:
    score = score_model.Score(**score_create.dict(),user_id = user_id)
    db.add(score)
    db.commit()
    db.refresh(score)
    return score