from typing import Optional

from pydantic import BaseModel, Field, field_validator


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: Optional[str] = Field(None, max_length=100, description="email")
    first_name: Optional[str] = Field(None, max_length=50, description="name")
    last_name: Optional[str] = Field(None, max_length=50, description="last name")
    password: str = Field(..., min_length=8, description="password")

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password should include at least 8 symbols')
        return v

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if v and '@' not in v:
            raise ValueError('Incorrect email')
        return v


class UserResponse(BaseModel):
    id: int
    username: str
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    telegram_id: Optional[int]
    is_active: bool

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str = Field(..., description="username")
    password: str = Field(..., description="password")


class UserUpdate(BaseModel):
    email: Optional[str] = Field(None, max_length=100, description="Email")
    first_name: Optional[str] = Field(None, max_length=50, description="name")
    last_name: Optional[str] = Field(None, max_length=50, description="last name")

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if v and '@' not in v:
            raise ValueError('Некорректный email адрес')
        return v
