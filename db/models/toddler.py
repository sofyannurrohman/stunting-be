from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.base import Base

class Toddler(Base):
    __tablename__ = "toddlers"

    id = Column(Integer, primary_key=True, index=True)
    age_months = Column(Integer)
    gender = Column(String(50))
    weight_kg = Column(Float)
    height_cm = Column(Float)
    predicted = Column(String(255))

    # ✅ Link to child profile
    profile_id = Column(Integer, ForeignKey("child_profiles.id"))
    profile = relationship("ChildProfile", back_populates="stunting_checks")

    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())
