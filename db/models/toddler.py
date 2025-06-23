from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.base import Base

class Toddler(Base):
    __tablename__ = "toddlers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Added length for VARCHAR
    age_months = Column(Integer)
    gender = Column(String(50))  # Added length for VARCHAR
    weight_kg = Column(Integer)
    height_cm = Column(Integer)
    predicted = Column(String(255))
    
    # Adding the relation to User model
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationship to User
    user = relationship("User", back_populates="toddlers")
    
    # Timestamps
    createdAt = Column(DateTime, server_default=func.now())  # Automatically set on insert
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())  # Automatically set on insert and update
