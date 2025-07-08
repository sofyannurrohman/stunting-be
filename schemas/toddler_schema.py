from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class ToddlerBase(BaseModel):
    gender: str
    name: str
    age_months: int
    height_cm: float
    weight_kg: float
    predicted: str | None = None

    # ✅ New optional fields
    nik: str | None = None
    tanggal_lahir: date | None = None
    tempat_lahir: str | None = None

class ToddlerCreate(BaseModel):
    name: str
    age_months: int
    gender: str
    weight_kg: float
    height_cm: float
    user_id: int
    predicted: str | None = None

    # ✅ New fields
    nik: str | None = None
    tanggal_lahir: date | None = None
    tempat_lahir: str | None = None

    class Config:
        orm_mode = True

class ToddlerUpdate(BaseModel):
    gender: str | None = None
    age_months: int | None = None
    height_cm: float | None = None
    weight_kg: float | None = None
    predicted: str | None = None

    # ✅ New fields
    nik: str | None = None
    tanggal_lahir: date | None = None
    tempat_lahir: str | None = None

class ToddlerRead(BaseModel):
    id: int
    name: str
    age_months: int
    gender: str
    weight_kg: float
    height_cm: float
    user_id: int
    predicted: str | None = None
    createdAt: datetime
    updatedAt: datetime

    # ✅ New fields
    nik: str | None = None
    tanggal_lahir: date | None = None
    tempat_lahir: str | None = None

    class Config:
        orm_mode = True

class ToddlerComparisonResponse(BaseModel):
    latest: Optional[ToddlerRead] = None
    previous: Optional[ToddlerRead] = None
