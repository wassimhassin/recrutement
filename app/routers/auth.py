# app/routers/auth.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.auth_controller import login, register
from app.schemas import UserCreate, UserLogin

router = APIRouter()

@router.post("/register")
async def user_register(user_data: UserCreate, db: Session = Depends(get_db)):
    return await register(user_data, db)

@router.post("/login")
async def user_login(user_data: UserLogin, db: Session = Depends(get_db)):
    return await login(user_data.username, user_data.password, db)
