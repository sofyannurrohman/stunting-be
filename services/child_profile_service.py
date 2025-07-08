from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models.child_profile import ChildProfile
from schemas.child_profile_schema import ChildProfileCreate, ChildProfileUpdate

async def create_child_profile(db: AsyncSession, profile_in: ChildProfileCreate):
    profile = ChildProfile(**profile_in.dict())
    db.add(profile)
    await db.commit()
    await db.refresh(profile)
    return profile

async def get_child_profile_by_nik(db: AsyncSession, nik: str):
    result = await db.execute(select(ChildProfile).where(ChildProfile.nik == nik))
    return result.scalar_one_or_none()

async def get_child_profile(db: AsyncSession, id: int):
    result = await db.execute(select(ChildProfile).where(ChildProfile.id == id))
    return result.scalar_one_or_none()

async def update_child_profile(db: AsyncSession, id: int, profile_in: ChildProfileUpdate):
    profile = await get_child_profile(db, id)
    if profile is None:
        return None
    for key, value in profile_in.dict(exclude_unset=True).items():
        setattr(profile, key, value)
    await db.commit()
    await db.refresh(profile)
    return profile

async def delete_child_profile(db: AsyncSession, id: int):
    profile = await get_child_profile(db, id)
    if profile is None:
        return None
    await db.delete(profile)
    await db.commit()
    return profile
