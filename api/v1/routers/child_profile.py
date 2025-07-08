from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.models.session import get_session
from schemas.child_profile_schema import (
    ChildProfileCreate,
    ChildProfileRead,
    ChildProfileUpdate,
)
from services.child_profile_service import (
    create_child_profile,
    get_child_profile,
    get_child_profile_by_nik,
    update_child_profile,
    delete_child_profile,
)

router = APIRouter()

@router.post("/child-profiles", response_model=ChildProfileRead, status_code=201)
async def create_profile(profile_in: ChildProfileCreate, db: AsyncSession = Depends(get_session)):
    existing = await get_child_profile_by_nik(db, profile_in.nik)
    if existing:
        raise HTTPException(status_code=400, detail="NIK already exists.")
    return await create_child_profile(db, profile_in)

@router.get("/child-profiles/{id}", response_model=ChildProfileRead)
async def read_profile(id: int, db: AsyncSession = Depends(get_session)):
    profile = await get_child_profile(db, id)
    if not profile:
        raise HTTPException(status_code=404, detail="Child profile not found.")
    return profile

@router.get("/child-profiles/by-nik/{nik}", response_model=ChildProfileRead)
async def read_profile_by_nik(nik: str, db: AsyncSession = Depends(get_session)):
    profile = await get_child_profile_by_nik(db, nik)
    if not profile:
        raise HTTPException(status_code=404, detail="Child profile not found.")
    return profile

@router.patch("/child-profiles/{id}", response_model=ChildProfileRead)
async def update_profile(id: int, profile_in: ChildProfileUpdate, db: AsyncSession = Depends(get_session)):
    updated = await update_child_profile(db, id, profile_in)
    if not updated:
        raise HTTPException(status_code=404, detail="Child profile not found.")
    return updated

@router.delete("/child-profiles/{id}", response_model=dict)
async def delete_profile(id: int, db: AsyncSession = Depends(get_session)):
    deleted = await delete_child_profile(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Child profile not found.")
    return {"message": "Child profile deleted successfully"}
