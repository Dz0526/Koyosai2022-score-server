from sqlalchemy.ext.asyncio import AsyncSession

import api.models.user as user_model
import api.schemas.user as user_schema

from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result

async def create(
    db: AsyncSession, user_create: user_schema.User
) -> user_model.User:
    user = user_model.User(**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

async def gets(db: AsyncSession) -> List[Tuple[int, str]]:
    result: Result = (
        db.execute(
            select(
                user_model.User.id,
                user_model.User.name,
            )
        )
    )
    return result.all()

async def get(db: AsyncSession, user_id: int) -> Optional[user_model.User]:
    result: Result = db.execute(
        select(user_model.User).filter(user_model.User.id == user_id)
    )
    user: Optional[Tuple[user_model.User]] = result.first()
    return user[0] if user is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

async def get_by_name(name: str, db: AsyncSession):
    result: Result = db.execute(select(user_model.User).filter(user_model.User.name == name))

    return result.first()[0]


async def update(
    db: AsyncSession, user_create: user_schema.UserCreate, original: user_model.User
) -> user_model.User:
    original.name = user_create.name
    db.add(original)
    db.commit()
    db.refresh(original)
    return original

async def delete(db: AsyncSession, original: user_model.User) -> None:
    db.delete(original)
    db.commit()
