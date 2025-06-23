from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class ToddlerBase(BaseModel):
    gender: str
    name:str
    age_months: int
    height_cm: float
    weight_kg: float
    predicted: str | None = None

class ToddlerCreate(BaseModel):
    name: str
    age_months: int
    gender: str
    weight_kg: float
    height_cm: float
    user_id: int  # Add this field if it's passed from the client
    predicted: str | None = None
    class Config:
        orm_mode = True

class ToddlerUpdate(BaseModel):
    gender: str | None = None
    age_months: int | None = None
    height_cm: float | None = None
    weight_kg: float | None = None
    predicted: str | None = None

class ToddlerRead(BaseModel):
    id: int
    name: str
    age_months: int
    gender: str
    weight_kg: float
    height_cm: float
    user_id: int  # Include user_id if you want to show the associated user
    predicted: str | None = None
    createdAt: datetime  # Add createdAt field
    updatedAt: datetime  
    class Config:
        orm_mode = True

class ToddlerComparisonResponse(BaseModel):
    latest: Optional[ToddlerRead] = None
    previous: Optional[ToddlerRead] = None