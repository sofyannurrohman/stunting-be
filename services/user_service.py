from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models.user import User
from schemas.user_schema import UserCreate, UserUpdate
from utils.security import hash_password

async def create_user(db: AsyncSession, user_in: UserCreate):
    hashed_password = hash_password(user_in.password)
    new_user = User(
        email=user_in.email,
        name=user_in.name,
        role=user_in.role,
        hashed_password=hashed_password,
        rt=user_in.rt,
        rw=user_in.rw
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

async def get_all_users(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(User).offset(skip).limit(limit))
    users = result.scalars().all()
    for user in users:
        if user.name is None:
            user.name = "Unknown"  # or any default
    return users

async def update_user(db: AsyncSession, user_id: int, user_in: UserUpdate):
    user = await get_user(db, user_id)
    if not user:
        return None
    for key, value in user_in.dict().items():
        setattr(user, key, value)
    await db.commit()
    await db.refresh(user)
    return user

async def delete_user(db: AsyncSession, user_id: int):
    user = await get_user(db, user_id)
    if not user:
        return None
    await db.delete(user)
    await db.commit()
    return user
