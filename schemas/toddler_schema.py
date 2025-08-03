from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class ToddlerBase(BaseModel):
    gender: str
    age_months: int
    height_cm: float
    weight_kg: float
    predicted: str | None = None
    profile_id: int
    # ✅ New optional fields

class ToddlerCreate(BaseModel):
    age_months: int
    gender: str
    weight_kg: float
    height_cm: float
    predicted: str | None = None
    profile_id: int

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
    age_months: int
    gender: str
    weight_kg: float
    height_cm: float
    predicted: str | None = None
    createdAt: datetime
    updatedAt: datetime
    profile_id: int

    class Config:
        orm_mode = True

class ToddlerComparisonResponse(BaseModel):
    latest: Optional[ToddlerRead] = None
    previous: Optional[ToddlerRead] = None
