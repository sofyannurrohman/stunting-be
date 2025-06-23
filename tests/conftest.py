import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app import app
from db.models.session import get_session
from db.base import Base
from httpx import AsyncClient
from httpx import ASGITransport
import os
from unittest.mock import AsyncMock

# ⚠️ Import the actual instance, not the module
from services.stunting_service import StuntingService


DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine_test = create_async_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
TestSessionLocal = async_sessionmaker(bind=engine_test, expire_on_commit=False)

async def override_get_db():
    async with TestSessionLocal() as session:
        yield session

@pytest_asyncio.fixture(scope="session", autouse=True)
async def prepare_database():
    os.makedirs("static/uploads", exist_ok=True)

    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture
async def async_client(prepare_database):
    app.dependency_overrides[get_session] = override_get_db
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

@pytest_asyncio.fixture(autouse=True)
async def mock_predict_once(monkeypatch):
    async def fake_predict_once(self, data, db):
        return {
            "prediction": "Stunting detected.",
            "gpt_response": "Please consult a doctor."
        }

    monkeypatch.setattr(StuntingService, "predict_once", fake_predict_once)


