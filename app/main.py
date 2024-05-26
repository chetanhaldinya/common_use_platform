from fastapi import FastAPI
from app.api.routes import user

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}
