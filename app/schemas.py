from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    date_of_birth: date
    phone: str

class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str
