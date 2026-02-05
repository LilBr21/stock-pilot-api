# TODO: Implement auth endpoint tests
#
# import pytest
#
# @pytest.mark.asyncio
# async def test_register_user(client):
#     response = await client.post("/api/v1/auth/register", json={
#         "email": "test@example.com",
#         "password": "testpassword123",
#         "full_name": "Test User"
#     })
#     assert response.status_code == 200
#     data = response.json()
#     assert data["email"] == "test@example.com"
#     assert "id" in data
#
# @pytest.mark.asyncio
# async def test_register_duplicate_email(client):
#     # Register first user
#     await client.post("/api/v1/auth/register", json={
#         "email": "test@example.com",
#         "password": "testpassword123"
#     })
#     # Try to register again with same email
#     response = await client.post("/api/v1/auth/register", json={
#         "email": "test@example.com",
#         "password": "differentpassword"
#     })
#     assert response.status_code == 400
#
# @pytest.mark.asyncio
# async def test_login_success(client):
#     # Register user first
#     await client.post("/api/v1/auth/register", json={
#         "email": "test@example.com",
#         "password": "testpassword123"
#     })
#     # Login
#     response = await client.post("/api/v1/auth/login", data={
#         "username": "test@example.com",
#         "password": "testpassword123"
#     })
#     assert response.status_code == 200
#     data = response.json()
#     assert "access_token" in data
#     assert "refresh_token" in data
#
# @pytest.mark.asyncio
# async def test_login_invalid_credentials(client):
#     response = await client.post("/api/v1/auth/login", data={
#         "username": "nonexistent@example.com",
#         "password": "wrongpassword"
#     })
#     assert response.status_code == 401
