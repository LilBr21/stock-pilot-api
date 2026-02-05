# TODO: Implement AuthService
#
# class AuthService:
#     def __init__(self, db: AsyncSession):
#         self.db = db
#
#     async def authenticate_user(self, email: str, password: str) -> User | None:
#         # Get user by email, verify password
#         pass
#
#     async def create_user(self, user_create: UserCreate) -> User:
#         # Hash password, create user in DB
#         pass
#
#     def create_tokens(self, user: User) -> Token:
#         # Create access + refresh tokens for user
#         pass
#
#     async def refresh_access_token(self, refresh_token: str) -> Token:
#         # Validate refresh token, create new token pair
#         pass
