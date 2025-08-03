from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models.information import Information
from schemas.information_schema import InformationCreate, InformationUpdate
from fastapi import UploadFile

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

async def update_information(
    db: AsyncSession,
    info_id: int,
    info_in,
    image=None
):
    # 1. Fetch the existing record
    result = await db.execute(select(Information).where(Information.id == info_id))
    info = result.scalars().first()
    if not info:
        return None

    # 2. If new image uploaded, save and update image_url
    if image:
        ext = os.path.splitext(image.filename)[1]
        unique_name = f"{uuid4().hex}{ext}"
        save_dir = "static/uploads"
        os.makedirs(save_dir, exist_ok=True)  # ensure folder exists
        save_path = os.path.join(save_dir, unique_name)

        # Save file content
        content = await image.read()
        with open(save_path, "wb") as f:
            f.write(content)

        # Update image_url field
        info.image_url = f"/static/uploads/{unique_name}"

    # 3. Update other fields if provided
    if info_in.title is not None:
        info.title = info_in.title
    if info_in.content is not None:
        info.content = info_in.content
    if info_in.category is not None:
        info.category = info_in.category
    if info_in.source is not None:
        info.source = info_in.source

    # 4. Commit changes
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
