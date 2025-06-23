from pydantic import BaseModel

from datetime import datetime
class InformationBase(BaseModel):
    title: str
    content: str
    category: str | None = None
    source: str
class InformationCreate(InformationBase):
    pass  # we won't use this for the file upload anymore; use FastAPI form handling.

class InformationUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    category: str | None = None
    source: str | None = None
class InformationRead(InformationBase):
    id: int
    image_url: str | None = None
    createdAt: datetime
    updatedAt: datetime  
    class Config:
        orm_mode = True
