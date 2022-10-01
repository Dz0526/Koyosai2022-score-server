from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.score as score_crud
from db.database import get_db
import api.schemas.score as score_schema
from typing import List

router = APIRouter()

@router.get("/users/{user_id}/scores",response_model=List[score_schema.Score])
async def user_scores(user_id: int, db: AsyncSession = Depends(get_db)):
    return await score_crud.get_user_score(db,user_id)

@router.post("/users/{user_id}/scores",response_model=score_schema.ScoreCreateResponse)
async def create_score(user_id: int, score_body: score_schema.ScoreCreate,db: AsyncSession = Depends(get_db)):
    return await score_crud.create_user_score(db, score_body, user_id)
