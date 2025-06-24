import joblib
import pandas as pd
import os
from openai import OpenAI
from schemas.stunting import StuntingInput
from services.toddler_service import *
from sqlalchemy.ext.asyncio import AsyncSession
from dotenv import load_dotenv
from typing import AsyncGenerator
import json


# Load the model, scaler, and label encoder once at module level
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')
le_condition = joblib.load('le_condition.joblib')
load_dotenv()
# Initialize OpenAI
AI_MODEL = os.getenv("AI_MODEL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Raise clear error if missing
if not OPENAI_API_KEY:
    raise EnvironmentError("Environment variable OPENAI_API_KEY is not set.")

# Initialize OpenAI client
openai = OpenAI(api_key=OPENAI_API_KEY)


class StuntingService:
    def __init__(self):
        self.model = model
        self.scaler = scaler
        self.le_condition = le_condition
        self.system_prompt = (
            "Anda adalah seorang ahli gizi profesional yang berfokus pada kesehatan dan nutrisi balita (usia 6 bulan - 5 tahun). "
            "Tugasmu adalah memberikan rekomendasi makanan sehat berdasarkan informasi yang diberikan pengguna. Gunakan bahasa yang sopan, jelas, dan mudah dipahami oleh orang tua. "
            "Jangan memberikan informasi medis tanpa menyarankan konsultasi ke dokter jika diperlukan."
        )

    def generate_user_prompt(self, usia, jenis_kelamin, berat_badan, tinggi_badan,
                             kondisi_kesehatan, makanan_favorit, makanan_tidak_disukai,
                             pantangan, gaya_hidup, preferensi_menu):
        return f"""
Berikut data balita saya:
- Usia: {usia} bulan
- Jenis kelamin: {jenis_kelamin}
- Berat: {berat_badan} kg
- Tinggi: {tinggi_badan} cm
- Kondisi kesehatan: {", ".join(kondisi_kesehatan) if kondisi_kesehatan else "Tidak ada"}
- Makanan favorit: {", ".join(makanan_favorit) if makanan_favorit else "Tidak ada"}
- Makanan tidak disukai: {", ".join(makanan_tidak_disukai) if makanan_tidak_disukai else "Tidak ada"}
- Pantangan: {", ".join(pantangan) if pantangan else "Tidak ada"}
- Gaya hidup: {gaya_hidup}
- Preferensi menu: {", ".join(preferensi_menu) if preferensi_menu else "Tidak ada"}

Tolong berikan **rekomendasi menu sehat** untuk balita ini, dengan:
1. **Menu 3 hari** (sarapan, makan siang, makan malam)
2. Disesuaikan dengan usia, kondisi kesehatan dan preferensi
3. Variatif dan bernutrisi seimbang
4. Ditampilkan dalam format JSON
5. Beri **penjelasan singkat (1-2 kalimat)** tentang manfaat nutrisi setiap menu dan kenapa balita ini membutuhkan nutrisi tersebut.  

**Format JSON yang diharapkan:**
{{
  "menu": [
    {{
      "hari": "Senin",
      "sarapan": {{
        "menu": "...",
        "nutrisi": "..."
      }},
      "makan_siang": {{
        "menu": "...",
        "nutrisi": "..."
      }},
      "makan_malam": {{
        "menu": "...",
        "nutrisi": "..."
      }}
    }}
  ]
}}
""".strip()

    async def predict_once(self, data: StuntingInput, db: AsyncSession) -> AsyncGenerator[str, None]:
        gender_mapping = {"Laki-laki": 0, "Perempuan": 1}

        if data.gender not in gender_mapping:
            yield json.dumps({"error": "Invalid input: Gender not recognized"}) + "\n"
            return

        try:
            gender_encoded = gender_mapping[data.gender]

            # --- Prediction logic ---
            input_df = pd.DataFrame(
                [[gender_encoded, data.age_months, data.height_cm, data.weight_kg]],
                columns=["Jenis Kelamin", "Umur (bulan)", "Tinggi Badan (cm)", "Berat Badan (kg)"]
            )

            input_scaled = self.scaler.transform(input_df)
            raw_prediction = self.model.predict(input_scaled)
            decoded_prediction = self.le_condition.inverse_transform([raw_prediction[0]])
            prediction_result = decoded_prediction[0]

            # Save to DB
            toddler_in = ToddlerCreate(
                name=data.name,
                user_id=data.user_id,
                gender=data.gender,
                age_months=data.age_months,
                height_cm=data.height_cm,
                weight_kg=data.weight_kg,
                predicted=prediction_result
            )
            await create_toddler(db, toddler_in)

            # --- GPT Completion ---
            prompt = self.generate_user_prompt(
                data.age_months, data.gender, data.weight_kg, data.height_cm,
                getattr(data, "kondisi_kesehatan", None),
                getattr(data, "makanan_favorit", None),
                getattr(data, "makanan_tidak_disukai", None),
                getattr(data, "pantangan", None),
                getattr(data, "gaya_hidup", None),
                getattr(data, "preferensi_menu", None)
            )

            response = openai.chat.completions.create(
                model=AI_MODEL,
                stream=True,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )

            gpt_response = ""
            for chunk in response:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    gpt_response += delta.content
            
            # Optional: strip whitespace/newlines
            gpt_response = gpt_response.strip()
            
            try:
                gpt_json = json.loads(gpt_response)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
                print("Raw GPT response:", gpt_response)
                gpt_json = {"error": "Failed to parse GPT response as JSON"}
            
            final_response = {
                    "prediction": prediction_result,
                    "gpt_response": gpt_json
                }

            yield json.dumps(final_response) + "\n"

        except Exception as e:
            yield json.dumps({"error": f"Prediction error: {str(e)}"}) + "\n"

stunting_service = StuntingService()
