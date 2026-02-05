# TODO: Implement stock endpoint tests
#
# import pytest
# from unittest.mock import AsyncMock, patch
#
# @pytest.mark.asyncio
# async def test_search_stocks(client, auth_headers):
#     # Mock the Finnhub API response
#     with patch("app.services.market_service.StockService.search_stocks") as mock_search:
#         mock_search.return_value = [
#             {"symbol": "AAPL", "description": "Apple Inc", "type": "Common Stock"}
#         ]
#         response = await client.get("/api/v1/stocks/search?q=AAPL", headers=auth_headers)
#         assert response.status_code == 200
#
# @pytest.mark.asyncio
# async def test_get_stock_quote(client, auth_headers):
#     # Mock the Finnhub API response
#     with patch("app.services.market_service.StockService.get_quote") as mock_quote:
#         mock_quote.return_value = {
#             "symbol": "AAPL",
#             "current_price": 150.0,
#             "change": 2.5,
#             "percent_change": 1.7
#         }
#         response = await client.get("/api/v1/stocks/AAPL", headers=auth_headers)
#         assert response.status_code == 200
#
# # Helper fixture for authenticated requests
# @pytest.fixture
# async def auth_headers(client):
#     # Register and login user
#     await client.post("/api/v1/auth/register", json={
#         "email": "test@example.com",
#         "password": "testpassword123"
#     })
#     response = await client.post("/api/v1/auth/login", data={
#         "username": "test@example.com",
#         "password": "testpassword123"
#     })
#     token = response.json()["access_token"]
#     return {"Authorization": f"Bearer {token}"}
