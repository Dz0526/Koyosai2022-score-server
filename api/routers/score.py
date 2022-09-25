from fastapi import APIRouter
import api.schemas.user as user_schema


router = APIRouter()

@router.get("/users/{user_id}/scores",response_model=user_schema.User)
async def user_scores():
    pass

@router.post("/users/{user_id}/scores",response_model=user_schema.User)
async def add_score():
    pass

