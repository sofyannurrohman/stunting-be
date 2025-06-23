from pydantic import BaseModel
from schemas.user_schema import UserRead

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserRead

    class Config:
        from_attributes = True
