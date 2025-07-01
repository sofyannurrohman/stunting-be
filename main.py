import os
from fastapi import FastAPI, Depends, Request
from api.v1.routers import predict
from api.v1.routers import user, toddler, information, auth, admin
from db.models.user import User
from utils.dependencies import get_current_user
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from alembic import command
from alembic.config import Config
from fastapi.responses import RedirectResponse
app = FastAPI()

# Mount static files (if needed)
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS setup

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "null"],  # Ganti ini dengan domain spesifik untuk security lebih baik
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Force HTTPS for all requests
@app.middleware("http")
async def force_https(request: Request, call_next):
    if request.headers.get("x-forwarded-proto", "http") != "https":
        url = request.url._url.replace("http://", "https://")
        return RedirectResponse(url, status_code=307)
    response = await call_next(request)
    # Ensure response headers use HTTPS
    if "location" in response.headers and response.headers["location"].startswith("http://"):
        response.headers["location"] = response.headers["location"].replace("http://", "https://")
    return response

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
app.include_router(toddler.router, prefix="/api/v1")
app.include_router(information.router, prefix="/api/v1")
app.include_router(predict.router, prefix="/api/v1")
app.include_router(admin.router, prefix="/api/v1")
# Sample protected endpoint
@app.get("/me")
def read_user(current_user: User = Depends(get_current_user)):
    return {"email": current_user.email}
@app.get("/")
def health_check():
    return {"status": "ok"}
@app.get("/init-db")
async def init_db():
    try:
        # override URL untuk migration agar pakai pymysql
        raw_url = os.getenv("DATABASE_URL").replace("aiomysql", "pymysql")
        
        alembic_cfg = Config("alembic.ini")
        alembic_cfg.set_main_option("sqlalchemy.url", raw_url)
        command.upgrade(alembic_cfg, "head")

        return {"message": "Migration successful"}
    
    except Exception as e:
        print("Error during alembic upgrade:", str(e))
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))