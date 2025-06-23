from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)  # Added length for VARCHAR
    name = Column(String(255))  # Added length for VARCHAR
    hashed_password = Column(String(255))  # Added length for VARCHAR
   
    # Timestamps
    createdAt = Column(DateTime, server_default=func.now())  # Automatically set on insert
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())  # Automatically set on insert and update
    role = Column(String(20), nullable=False, default="user")

# One-to-Many Relationship to Toddler
    toddlers = relationship("Toddler", back_populates="user", cascade="all, delete-orphan")