from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models.toddler import Toddler
from schemas.toddler_schema import ToddlerCreate, ToddlerUpdate
from sqlalchemy import desc
from fastapi import HTTPException

async def create_toddler(db: AsyncSession, toddler_in: ToddlerCreate):
    db_toddler = Toddler(
        name=toddler_in.name,
        age_months=toddler_in.age_months,
        gender=toddler_in.gender,
        weight_kg=toddler_in.weight_kg,
        height_cm=toddler_in.height_cm,
        user_id=toddler_in.user_id  # Associating the toddler with the parent user
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
        select(Toddler).where(Toddler.user_id == user_id)
    )
    toddlers = result.scalars().all()
    print("Found toddlers:", toddlers)
    return toddlers

async def get_latest_two_by_toddler_name(db: AsyncSession, toddler_name: str, user_id: int):
    # Find the toddler for this user
    result = await db.execute(
        select(Toddler).filter(
            Toddler.name == toddler_name,
            Toddler.user_id == user_id
        )
    )
    toddler = result.scalars().first()
    if not toddler:
        raise HTTPException(status_code=404, detail="Toddler not found")

    # Get the latest two data entries
    result = await db.execute(
    select(Toddler).where(Toddler.name == toddler_name).order_by(desc(Toddler.createdAt)))
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