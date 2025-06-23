from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models.information import Information
from schemas.information_schema import InformationCreate, InformationUpdate

async def create_information(db: AsyncSession, info_in: dict):
    new_info = Information(**info_in)
    db.add(new_info)
    await db.commit()
    await db.refresh(new_info)
    return new_info

async def get_information(db: AsyncSession, info_id: int):
    result = await db.execute(select(Information).filter(Information.id == info_id))
    return result.scalar_one_or_none()

async def get_all_information(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Information).offset(skip).limit(limit))
    return result.scalars().all()

async def update_information(db: AsyncSession, info_id: int, info_in: InformationUpdate):
    info = await get_information(db, info_id)
    if not info:
        return None
    for key, value in info_in.dict(exclude_unset=True).items():
        setattr(info, key, value)
    await db.commit()
    await db.refresh(info)
    return info

async def delete_information(db: AsyncSession, info_id: int):
    info = await get_information(db, info_id)
    if not info:
        return None
    await db.delete(info)
    await db.commit()
    return info
