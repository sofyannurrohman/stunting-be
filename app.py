from fastapi import FastAPI, Depends
from api.v1.routers import predict
from api.v1.routers import user, toddler, information, auth
from db.models.user import User
from utils.dependencies import get_current_user
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
origins = [
    "http://localhost:5173",  # Vite dev server
    # Add more if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["*"] to allow all (less secure)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router, prefix="/api/v1")

@app.get("/me")
def read_user(current_user: User = Depends(get_current_user)):
    return {"email": current_user.email}
app.include_router(user.router, prefix="/api/v1")
app.include_router(toddler.router, prefix="/api/v1")
app.include_router(information.router, prefix="/api/v1")
app.include_router(predict.router, prefix="/api/v1")
