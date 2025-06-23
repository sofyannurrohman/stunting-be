# schemas/user.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    name: str
    role: str
    password: str

class UserRead(BaseModel):
    id: int
    email: str
    name: str
    role: str
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: str | None = None

class UserOut(BaseModel):
    id: int

    class Config:
        orm_mode = True
