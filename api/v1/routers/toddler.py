from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.models.session import get_session
from schemas.toddler_schema import ToddlerCreate, ToddlerRead, ToddlerUpdate, ToddlerComparisonResponse
from services import toddler_service
from typing import List

router = APIRouter(prefix="/toddlers", tags=["Toddlers"])

@router.post("/", response_model=ToddlerRead, status_code=201)
async def create_toddler(toddler_in: ToddlerCreate, db: AsyncSession = Depends(get_session)):
    return await toddler_service.create_toddler(db, toddler_in)

@router.get("/{toddler_id}", response_model=ToddlerRead)
async def get_toddler(toddler_id: int, db: AsyncSession = Depends(get_session)):
    toddler = await toddler_service.get_toddler(db, toddler_id)
    if not toddler:
        raise HTTPException(status_code=404, detail="Toddler not found")
    return toddler

@router.get("/", response_model=List[ToddlerRead])
async def list_toddlers(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    return await toddler_service.get_all_toddlers(db, skip=skip, limit=limit)

@router.get("/users/{user_id}", response_model=List[ToddlerRead])
async def user_toddlers(user_id: int, db: AsyncSession = Depends(get_session)):
    return await toddler_service.get_user_toddlers(db, user_id)

@router.get("/growth/users", response_model=ToddlerComparisonResponse)
async def compare_toddler_data(
    user_id: int,
    toddler_name: str,
    db: AsyncSession = Depends(get_session)
):
    return await toddler_service.get_latest_two_by_toddler_name(db, toddler_name, user_id)

@router.put("/{toddler_id}", response_model=ToddlerRead)
async def update_toddler(toddler_id: int, toddler_in: ToddlerUpdate, db: AsyncSession = Depends(get_session)):
    toddler = await toddler_service.update_toddler(db, toddler_id, toddler_in)
    if not toddler:
        raise HTTPException(status_code=404, detail="Toddler not found")
    return toddler

@router.delete("/{toddler_id}", response_model=ToddlerRead)
async def delete_toddler(toddler_id: int, db: AsyncSession = Depends(get_session)):
    toddler = await toddler_service.delete_toddler(db, toddler_id)
    if not toddler:
        raise HTTPException(status_code=404, detail="Toddler not found")
    return toddler
