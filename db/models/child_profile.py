from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class ChildProfile(Base):
    __tablename__ = "child_profiles"

    id = Column(Integer, primary_key=True, index=True)
    nik = Column(String(20), unique=True, nullable=False)
    name = Column(String(255))
    tanggal_lahir = Column(Date)
    tempat_lahir = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id"))

    # relationship to User
    user = relationship("User", back_populates="child_profiles")

    # relationship to Toddler (stunting history)
    stunting_checks = relationship("Toddler", back_populates="profile")
