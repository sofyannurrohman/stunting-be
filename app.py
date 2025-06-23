import os
from fastapi import FastAPI, Depends
from api.v1.routers import predict
from api.v1.routers import user, toddler, information, auth
from db.models.user import User
from utils.dependencies import get_current_user
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from alembic import command
from alembic.config import Config
app = FastAPI()

# Mount static files (if needed)
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS setup
origins = [
    "http://localhost:5173",  # Vite dev server
    # Tambahkan domain frontend production jika sudah ada
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti ini dengan domain spesifik untuk security lebih baik
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
app.include_router(toddler.router, prefix="/api/v1")
app.include_router(information.router, prefix="/api/v1")
app.include_router(predict.router, prefix="/api/v1")

# Sample protected endpoint
@app.get("/me")
def read_user(current_user: User = Depends(get_current_user)):
    return {"email": current_user.email}

@app.get("/init-db")
async def init_db():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))
    command.upgrade(alembic_cfg, "head")
    return {"message": "Migration done"}
# ✅ Tambahkan block ini agar bisa run di Railway
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # PORT akan di-set otomatis oleh Railway
    uvicorn.run("app:app", host="0.0.0.0", port=port)
