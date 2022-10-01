from fastapi import APIRouter
import api.schemas.ranking as ranking_schema
from typing import List

router = APIRouter()

@router.get("/users/{user_id}/ranking",response_model=ranking_schema.Ranking)
async def list_ranking():
    pass