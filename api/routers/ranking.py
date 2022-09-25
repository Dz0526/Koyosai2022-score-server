from fastapi import APIRouter
import api.schemas.user as user_schema

router = APIRouter()

@router.get("/users/{user_id}/ranking",response_model=user_schema.User)
async def list_ranking():
    pass