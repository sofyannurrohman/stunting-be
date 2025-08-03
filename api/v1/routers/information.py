from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.models.session import get_session
from schemas.information_schema import InformationCreate, InformationRead, InformationUpdate
from services import information_service
from fastapi import UploadFile, File, Form
import os
from uuid import uuid4

router = APIRouter(prefix="/information", tags=["Information"])

@router.post("/", response_model=InformationRead)
async def create_information(
    title: str = Form(...),
    content: str = Form(...),
    category: str = Form(None),
    source: str = Form(...),
    image: UploadFile = File(None),
    db: AsyncSession = Depends(get_session)
):
    image_url = None
    if image:
        ext = os.path.splitext(image.filename)[1]
        unique_name = f"{uuid4().hex}{ext}"
        save_path = os.path.join("static/uploads", unique_name)
        
        # Save file
        with open(save_path, "wb") as f:
            f.write(await image.read())
        
        image_url = f"/static/uploads/{unique_name}"  # Or your actual URL

    info_in = {
        "title": title,
        "content": content,
        "category": category,
        "source": source,
        "image_url": image_url,
    }
    return await information_service.create_information(db, info_in)

@router.get("/{info_id}", response_model=InformationRead)
async def get_information(info_id: int, db: AsyncSession = Depends(get_session)):
    info = await information_service.get_information(db, info_id)
    if not info:
        raise HTTPException(status_code=404, detail="Information not found")
    return info

@router.get("/", response_model=list[InformationRead])
async def list_information(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    return await information_service.get_all_information(db, skip=skip, limit=limit)

@router.put("/{info_id}", response_model=InformationRead)
async def update_information(
    info_id: int,
    title: str = Form(None),
    content: str = Form(None),
    category: str = Form(None),
    source: str = Form(None),
    image: UploadFile | None = File(None),
    db: AsyncSession = Depends(get_session)
):
    info_in = InformationUpdate(
        title=title,
        content=content,
        category=category,
        source=source
    )
    info = await information_service.update_information(db, info_id, info_in, image)
    if not info:
        raise HTTPException(status_code=404, detail="Information not found")
    return info


@router.delete("/{info_id}", response_model=InformationRead)
async def delete_information(info_id: int, db: AsyncSession = Depends(get_session)):
    info = await information_service.delete_information(db, info_id)
    if not info:
        raise HTTPException(status_code=404, detail="Information not found")
    return info
