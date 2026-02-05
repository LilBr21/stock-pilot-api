# TODO: Implement shared dependencies for dependency injection
#
# async def get_db() -> AsyncGenerator[AsyncSession, None]:
#     # Yield database session
#     pass
#
# async def get_current_user(
#     token: str = Depends(oauth2_scheme),
#     db: AsyncSession = Depends(get_db)
# ) -> User:
#     # Decode token, get user from DB
#     # Raise HTTPException(401) if invalid
#     pass
#
# async def get_current_active_user(
#     current_user: User = Depends(get_current_user)
# ) -> User:
#     # Check if user is active
#     # Raise HTTPException(400) if inactive
#     pass
#
# Hints:
# from fastapi.security import OAuth2PasswordBearer
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
