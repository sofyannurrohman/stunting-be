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
    get_child_profiles_by_user_id,
    get_all_child_profiles
)

router = APIRouter(prefix="/child-profiles", tags=["Child Profiles"])

@router.post("/", response_model=ChildProfileRead, status_code=201)
async def create_profile(profile_in: ChildProfileCreate, db: AsyncSession = Depends(get_session)):
    existing = await get_child_profile_by_nik(db, profile_in.nik)
    if existing:
        raise HTTPException(status_code=400, detail="NIK already exists.")
    return await create_child_profile(db, profile_in)

@router.get("/", response_model=list[ChildProfileRead])
async def read_all_child_profiles(db: AsyncSession = Depends(get_session)):
    profiles = await get_all_child_profiles(db)
    if not profiles:
        raise HTTPException(status_code=404, detail="Child profile not found.")
    return profiles

@router.get("/user/{user_id}", response_model=list[ChildProfileRead])
async def read_child_profiles_by_user(user_id: int, db: AsyncSession = Depends(get_session)):
    profiles = await get_child_profiles_by_user_id(db, user_id)
    if not profiles:
        raise HTTPException(status_code=404, detail="Child profile not found.")
    return profiles

@router.get("/{id}", response_model=ChildProfileRead)
async def read_profile(id: int, db: AsyncSession = Depends(get_session)):
    profile = await get_child_profile(db, id)
    if not profile:
        raise HTTPException(status_code=404, detail="Child profile not found.")
    return profile

@router.get("/by-nik/{nik}", response_model=ChildProfileRead)
async def read_profile_by_nik(nik: str, db: AsyncSession = Depends(get_session)):
    profile = await get_child_profile_by_nik(db, nik)
    if not profile:
        raise HTTPException(status_code=404, detail="Child profile not found.")
    return profile

@router.patch("/{id}", response_model=ChildProfileRead)
async def update_profile(id: int, profile_in: ChildProfileUpdate, db: AsyncSession = Depends(get_session)):
    updated = await update_child_profile(db, id, profile_in)
    if not updated:
        raise HTTPException(status_code=404, detail="Child profile not found.")
    return updated

@router.delete("/{id}", response_model=dict)
async def delete_profile(id: int, db: AsyncSession = Depends(get_session)):
    deleted = await delete_child_profile(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Child profile not found.")
    return {"message": "Child profile deleted successfully"}
