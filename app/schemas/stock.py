# TODO: Implement stock schemas with Pydantic v2
#
# Schemas to implement (based on Finnhub API responses):
#
# class StockQuote(BaseModel):
#     symbol: str
#     current_price: float  # c
#     change: float  # d
#     percent_change: float  # dp
#     high: float  # h
#     low: float  # l
#     open: float  # o
#     previous_close: float  # pc
#     timestamp: datetime  # t
#
# class StockSearchResult(BaseModel):
#     symbol: str
#     description: str
#     type: str
#
# class StockSearchResponse(BaseModel):
#     results: list[StockSearchResult]
#
# class CandleData(BaseModel):
#     timestamps: list[int]  # t
#     open: list[float]  # o
#     high: list[float]  # h
#     low: list[float]  # l
#     close: list[float]  # c
#     volume: list[int]  # v
