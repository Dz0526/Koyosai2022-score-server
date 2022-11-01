from functools import cache
from typing import List, Union

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

import api.cruds.user as user_crud
from db.database import get_db

import api.schemas.user as user_schema

router = APIRouter()


@router.get("/users", response_model=Union[List[user_schema.User], user_schema.User])
async def list_users(name: Union[str, None] = None, db: AsyncSession = Depends(get_db)):
    if name:
        try:
            user = await user_crud.get_by_name(name, db)
            return user
        except TypeError:
            raise HTTPException(status_code=404, detail="user not found")
    return await user_crud.gets(db)



@router.get("/users/{user_id}", response_model=user_schema.User)
async def simple_users(
    user_id: int, db: AsyncSession = Depends(get_db)
):
    return await user_crud.get(db,user_id=user_id)


@router.post("/users", response_model=user_schema.User)
async def create(user_body: user_schema.UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await user_crud.create(db, user_body)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User conflict")



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

