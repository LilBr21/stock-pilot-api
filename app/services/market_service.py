# TODO: Implement StockService (Finnhub integration)
#
# class StockService:
#     def __init__(self):
#         self.client = httpx.AsyncClient()
#         self.api_key = settings.finnhub_api_key
#         self.base_url = settings.finnhub_base_url
#
#     async def search_stocks(self, query: str) -> list[StockSearchResult]:
#         # GET /search?q={query}&token={api_key}
#         pass
#
#     async def get_quote(self, symbol: str) -> StockQuote:
#         # GET /quote?symbol={symbol}&token={api_key}
#         pass
#
#     async def get_candles(self, symbol: str, resolution: str, from_ts: int, to_ts: int) -> CandleData:
#         # GET /stock/candle?symbol={symbol}&resolution={resolution}&from={from}&to={to}&token={api_key}
#         # resolution: 1, 5, 15, 30, 60, D, W, M
#         pass
#
#     async def close(self):
#         await self.client.aclose()
