from fastapi import APIRouter, Depends
from schemas.stunting import StuntingInput
from services.stunting_service import stunting_service
from fastapi.responses import StreamingResponse
from schemas.stunting import StuntingInput
from db.models.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import StreamingResponse
router = APIRouter()

@router.post("/predict")
async def predict(data: StuntingInput, db: AsyncSession = Depends(get_session)):
    async def event_generator():
        async for chunk in stunting_service.predict_once(data, db):
            yield chunk

    return StreamingResponse(event_generator(), media_type="application/json")
