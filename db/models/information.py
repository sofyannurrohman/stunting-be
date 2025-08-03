from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from db.base import Base

class Information(Base):
    __tablename__ = "information"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Added length for VARCHAR columns
    title = Column(String(255))  # Added length for VARCHAR
    content = Column(Text)  # Added length for VARCHAR, content can be longer
    image_url = Column(String(255))  # Added length for VARCHAR
    category = Column(String(255))
    source = Column(String(255))
    # Timestamps
    createdAt = Column(DateTime, server_default=func.now())  # Automatically set on insert
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())  # Automatically set on insert and update
