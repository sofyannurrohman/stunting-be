from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.auth_schema import LoginRequest, TokenResponse
from schemas.user_schema import UserRead
from services.auth_service import authenticate_user
from db.models.session import get_session

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: Session = Depends(get_session)):
    access_token, user = await authenticate_user(request.email, request.password, db)
    return TokenResponse(access_token=access_token, user=UserRead.from_orm(user))

