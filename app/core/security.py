# TODO: Implement security utilities
#
# Functions to implement:
# 1. verify_password(plain_password: str, hashed_password: str) -> bool
#    - Use passlib with bcrypt
#
# 2. get_password_hash(password: str) -> str
#    - Use passlib with bcrypt
#
# 3. create_access_token(data: dict, expires_delta: timedelta | None = None) -> str
#    - Use python-jose to create JWT
#    - Include "exp" and "type": "access" in payload
#
# 4. create_refresh_token(data: dict, expires_delta: timedelta | None = None) -> str
#    - Similar to access token but with "type": "refresh"
#
# 5. decode_token(token: str) -> dict | None
#    - Decode and validate JWT, return None if invalid
#
# Hints:
# from jose import jwt
# from passlib.context import CryptContext
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
