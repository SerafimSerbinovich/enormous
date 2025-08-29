from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from core.database.database import get_db
from core.database.user import User


class UserCreate(BaseModel):
    username: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str | None
    first_name: str | None
    last_name: str | None
    telegram_id: int | None
    is_active: bool

    class Config:
        from_attributes = True


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/create", response_model=UserResponse)
async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    if user_data.email:
        existing_email = db.query(User).filter(User.email == user_data.email).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already registered")
    

    
    db_user = User(
        username=user_data.username,
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user
