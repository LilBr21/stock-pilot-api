import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator


class WatchlistBase(BaseModel):
    name: str = Field(max_length=255)


class WatchlistCreate(WatchlistBase):
    pass


class WatchlistUpdate(BaseModel):
    name: str | None = Field(default=None, max_length=255)


class WatchlistRead(WatchlistBase):
    id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class WatchlistItemBase(BaseModel):
    symbol: str = Field(max_length=10)
    # quantity: float = Field(..., gt=0)
    # purchase_price: float = Field(..., gt=0)


class WatchlistItemCreate(WatchlistItemBase):
    @field_validator("symbol")
    @classmethod
    def symbol_validation(cls, symbol: str) -> str:
        return symbol.strip().upper()


class WatchlistItemUpdate(BaseModel):
    # quantity: float | None = Field(default=None, gt=0)
    # purchase_price: float | None = Field(default=None, gt=0)
    pass


class WatchlistItemRead(WatchlistItemBase):
    id: uuid.UUID
    watchlist_id: uuid.UUID
    added_at: datetime

    model_config = ConfigDict(from_attributes=True)
