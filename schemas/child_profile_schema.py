from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class ChildProfileBase(BaseModel):
    nik: str = Field(..., min_length=16, max_length=20)
    name: str
    tanggal_lahir: date
    tempat_lahir: str
    user_id: int

class ChildProfileCreate(ChildProfileBase):
    pass

class ChildProfileUpdate(BaseModel):
    name: Optional[str] = None
    nik: Optional[str]
    tanggal_lahir: Optional[date] = None
    tempat_lahir: Optional[str] = None
    user_id: Optional[int] = None

class ChildProfileRead(ChildProfileBase):
    id: int

    class Config:
        from_attributes = True
