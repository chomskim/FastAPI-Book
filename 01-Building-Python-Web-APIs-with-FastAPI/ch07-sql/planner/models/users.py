
from typing import Optional, List

from fastapi import Form
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Column, JSON


from models.events import Event


class User(SQLModel, table=True):
    email: EmailStr = Field(...,primary_key=True)
    username: str = Field(...)
    password: str = Field(...)
    events: List[int] = Field(default=[], sa_column=Column(JSON))

    @classmethod
    def as_form(
            cls,
            email: EmailStr = Form(...),
            username: str = Form(...),
            password: str = Form(...)
    ):
        return cls(email=email, username=username, password=password)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@example.com",
                "username": "fastapiexample001",
                "password": "Str0ng!!",
            }
        }

class UserSignIn(SQLModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    @classmethod
    def as_form(
            cls,
            email: EmailStr = Form(...),
            password: str = Form(...)
    ):
        return cls(email=email, password=password)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
