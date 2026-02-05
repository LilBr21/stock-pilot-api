# TODO: Implement user schemas with Pydantic v2
#
# Schemas to implement:
#
# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str  # min 8 chars
#     full_name: str | None = None
#
# class UserRead(BaseModel):
#     id: UUID
#     email: EmailStr
#     full_name: str | None
#     is_active: bool
#     created_at: datetime
#
#     model_config = ConfigDict(from_attributes=True)
#
# class UserUpdate(BaseModel):
#     full_name: str | None = None
#     password: str | None = None  # for password change
