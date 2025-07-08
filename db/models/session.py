from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from databases import Database
from dotenv import load_dotenv
import os
from db.base import Base 
from db.models.user import User  # Ensure models are imported
from db.models.toddler import Toddler
from db.models.information import Information
from db.models.child_profile import ChildProfile
# Load environment variables from .env
load_dotenv()

# Fetch the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Async Database connection
database = Database(DATABASE_URL)

# SQLAlchemy async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Use this to create the async session
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency to get the session
async def get_session():
    async with async_session() as session:
        yield session