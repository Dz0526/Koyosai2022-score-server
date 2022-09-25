from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.user as user_crud
from db.database import get_db

import api.schemas.user as user_schema

router = APIRouter()


@router.get("/users", response_model=List[user_schema.User])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await user_crud.gets(db)



@router.get("/users/{user_id}", response_model=user_schema.User)
async def simple_users(
    user_id: int, db: AsyncSession = Depends(get_db)
):
    return await user_crud.get(db,user_id=user_id)



@router.get("/users/{user_id}/scores",response_model=user_schema.User)
async def user_scores():
    pass

@router.get("/users/{user_id}/ranking",response_model=user_schema.User)
async def list_ranking():
    pass



@router.post("/users", response_model=user_schema.User)
async def create(user_body: user_schema.UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_crud.create(db, user_body)




@router.post("/users/{user_id}/scores",response_model=user_schema.User)
async def add_score():
    pass




@router.put("/users/{user_id}", response_model=user_schema.User)
async def update(
    user_id: int, user_body: user_schema.UserCreate, db: AsyncSession = Depends(get_db)
):
    user = await user_crud.get(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return await user_crud.update(db, user_body, original=user)
    


@router.delete("/users/{user_id}")
async def delete(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return await user_crud.delete(db, original=user)

