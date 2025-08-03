from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models.toddler import Toddler
from db.models.child_profile import ChildProfile
from schemas.toddler_schema import ToddlerCreate, ToddlerUpdate
from sqlalchemy import desc
from fastapi import HTTPException

async def create_toddler(db: AsyncSession, toddler_in: ToddlerCreate):
    db_toddler = Toddler(
        age_months=toddler_in.age_months,
        gender=toddler_in.gender,
        weight_kg=toddler_in.weight_kg,
        height_cm=toddler_in.height_cm,
        predicted=toddler_in.predicted,
        profile_id=toddler_in.profile_id
    )
    db.add(db_toddler)
    await db.commit()
    await db.refresh(db_toddler)
    return db_toddler

async def get_toddler(db: AsyncSession, toddler_id: int):
    result = await db.execute(select(Toddler).filter(Toddler.id == toddler_id))
    return result.scalar_one_or_none()

async def get_all_toddlers(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Toddler).offset(skip).limit(limit))
    return result.scalars().all()

async def get_user_toddlers(db: AsyncSession, user_id: int):
    result = await db.execute(
        select(
            Toddler.id,
            Toddler.age_months,
            Toddler.gender,
            Toddler.weight_kg,
            Toddler.height_cm,
            Toddler.predicted,
            Toddler.profile_id,
            Toddler.createdAt,
            Toddler.updatedAt,
            ChildProfile.name.label("profile_name")  # ✅ add this
        )
        .join(ChildProfile, ChildProfile.id == Toddler.profile_id)
        .where(ChildProfile.user_id == user_id)
        .order_by(Toddler.createdAt.desc())
    )
    rows = result.all()
    return [
        {
            "id": row.id,
            "age_months": row.age_months,
            "gender": row.gender,
            "weight_kg": row.weight_kg,
            "height_cm": row.height_cm,
            "predicted": row.predicted,
            "profile_id": row.profile_id,
            "createdAt": row.createdAt,
            "updatedAt": row.updatedAt,
            "profile_name": row.profile_name  # ✅ return in dict
        }
        for row in rows
    ]
    

async def get_latest_two_by_profile_id(db: AsyncSession, profile_id: int):
    result = await db.execute(
        select(Toddler)
        .where(Toddler.profile_id == profile_id)
        .order_by(desc(Toddler.createdAt))
    )
    records = result.scalars().all()

    latest = records[0] if len(records) > 0 else None
    previous = records[1] if len(records) > 1 else None

    return {"latest": latest, "previous": previous}


async def update_toddler(db: AsyncSession, toddler_id: int, toddler_in: ToddlerUpdate):
    toddler = await get_toddler(db, toddler_id)
    if not toddler:
        return None
    for key, value in toddler_in.dict(exclude_unset=True).items():
        setattr(toddler, key, value)
    await db.commit()
    await db.refresh(toddler)
    return toddler

async def delete_toddler(db: AsyncSession, toddler_id: int):
    toddler = await get_toddler(db, toddler_id)
    if not toddler:
        return None
    await db.delete(toddler)
    await db.commit()
    return toddler