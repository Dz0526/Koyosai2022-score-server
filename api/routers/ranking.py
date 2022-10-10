from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.ranking as ranking_crud
import api.schemas.ranking as ranking_schema
from db.database import get_db
from typing import List
router = APIRouter()

@router.get("/ranking", response_model=List[ranking_schema.RankingBase])
async def list_ranking(db: AsyncSession = Depends(get_db)):
    return await ranking_crud.get_rank_list(db)

@router.get("/users/{user_id}/ranking",response_model=ranking_schema.Ranking)
async def user_ranking(user_id: int, db: AsyncSession = Depends(get_db)):
    return await ranking_crud.get_user_rank_list(db,user_id)

