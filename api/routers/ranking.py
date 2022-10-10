from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.ranking as ranking_crud
import api.schemas.ranking as ranking_schema
from db.database import get_db

router = APIRouter()

@router.get("/users/{user_id}/ranking",response_model=ranking_schema.Ranking)
async def list_ranking(user_id: int, db: AsyncSession = Depends(get_db)):
    return await ranking_crud.get_rank_list(db,user_id)

