"""Pydantic models for authentication flows."""

from pydantic import BaseModel, EmailStr, Field


class UserPublic(BaseModel):
    id: str = Field(..., description="Unique identifier for the user")
    email: EmailStr
    is_active: bool = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenPayload(BaseModel):
    access_token: str
    token_type: str = "bearer"
