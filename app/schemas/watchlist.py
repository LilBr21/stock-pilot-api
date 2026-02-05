# TODO: Implement watchlist schemas with Pydantic v2
#
# Schemas to implement:
#
# class WatchlistCreate(BaseModel):
#     name: str  # max 100 chars
#
# class WatchlistItemCreate(BaseModel):
#     symbol: str  # max 10 chars, uppercase
#
# class WatchlistItemRead(BaseModel):
#     id: UUID
#     symbol: str
#     added_at: datetime
#
#     model_config = ConfigDict(from_attributes=True)
#
# class WatchlistRead(BaseModel):
#     id: UUID
#     name: str
#     created_at: datetime
#     items: list[WatchlistItemRead] = []
#
#     model_config = ConfigDict(from_attributes=True)
