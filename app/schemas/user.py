from datetime import datetime
import re
import uuid
from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator


class UserBase(BaseModel):
    email: EmailStr = Field(max_length=255)
    display_name: str = Field(max_length=100)
    is_active: bool = True


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=100)

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not re.search(r'[A-Z]', password):
            raise ValueError('Password requires at least one uppercase letter')

        return password


class UserUpdate(BaseModel):
    email: EmailStr | None = Field(default=None, max_length=255)
    display_name: str | None = Field(default=None, max_length=100)
    password: str | None = Field(default=None, min_length=8, max_length=100)
    is_active: bool | None = Field(default=None)


class UserRead(UserBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
