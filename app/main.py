from fastapi import FastAPI
from app.routers import auth
from app.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

# auth router
app.include_router(auth.router, prefix="/api/auth")

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI project"}
