from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str = Field(None, example="伊藤大輝")

class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True