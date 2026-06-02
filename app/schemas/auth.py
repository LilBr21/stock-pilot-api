import uuid
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    subject: uuid.UUID = Field(validation_alias="sub")
    type: str
    expire: datetime = Field(validation_alias="exp")


class RefreshRequest(BaseModel):
    refresh_token: str
