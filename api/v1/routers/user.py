from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.models.session import get_session
from services.user_service import *
from schemas.user_schema import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
async def create_user_view(user_in: UserCreate, db: AsyncSession = Depends(get_session)):
    return await create_user(db, user_in)

@router.get("/{user_id}", response_model=UserRead)
async def read_user_view(user_id: int, db: AsyncSession = Depends(get_session)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[UserRead])
async def read_users(skip: int = 0, limit: int = 20, db: AsyncSession = Depends(get_session)):
    return await get_all_users(db, skip=skip, limit=limit)

@router.put("/{user_id}", response_model=UserRead)
async def update_user_view(user_id: int, user_in: UserCreate, db: AsyncSession = Depends(get_session)):
    user = await update_user(db, user_id, user_in)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", response_model=UserRead)
async def delete_user_view(user_id: int, db: AsyncSession = Depends(get_session)):
    user = await delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
