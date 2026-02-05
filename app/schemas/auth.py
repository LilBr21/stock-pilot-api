# TODO: Implement auth schemas with Pydantic v2
#
# Schemas to implement:
#
# class Token(BaseModel):
#     access_token: str
#     refresh_token: str
#     token_type: str = "bearer"
#
# class TokenPayload(BaseModel):
#     sub: str  # user id
#     type: str  # "access" or "refresh"
#     exp: datetime
#
# class LoginRequest(BaseModel):
#     email: EmailStr
#     password: str
#
# class RefreshRequest(BaseModel):
#     refresh_token: str
