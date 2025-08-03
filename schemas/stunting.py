from pydantic import BaseModel
from typing import List, Optional

class StuntingInput(BaseModel):
    age_months: int
    weight_kg: float
    height_cm: float
    gender: str
    kondisi_kesehatan: Optional[List[str]] = []
    makanan_favorit: Optional[List[str]] = []
    makanan_tidak_disukai: Optional[List[str]] = []
    pantangan: Optional[List[str]] = []
    gaya_hidup: Optional[str] = ""
    preferensi_menu: Optional[List[str]] = []
    profile_id: int

class StuntingPrediction(BaseModel):
    prediction: str
