from pydantic import BaseModel #, model_validator
from typing import List, Optional, Union

class Attribute(BaseModel):
    defindex: int
    value: Optional[Union[str, int, float]] = None
    float_value: Optional[Union[float, int]] = None

class Item(BaseModel):
    id: Optional[int] = None
    original_id: Optional[int] = None
    defindex: int
    quality: int
    quantity: Optional[Union[int, str]] = None
    attributes: List[Attribute] = []
    marketplace_price: Optional[Union[float, int]] = None
    marketplace_sku: Optional[str] = None

class Currencies(BaseModel):
    usd: Optional[float] = 0
    keys: Optional[float] = 0
    metal: Optional[Union[float, int]] = 0

    # @field_validator('keys')
    # @classmethod
    # def validate_keys(cls, v):
    #     if v is None:
    #         return v
    #     if isinstance(v, float):
    #         if v.is_integer():
    #             return int(v)
    #         raise ValueError("Keys must be a whole number")
    #     return v

class SnapshotListing(BaseModel):
    steamid: str
    offers: int
    buyout: int
    details: str
    intent: str
    timestamp: int
    price: float
    item: Item
    currencies: Currencies
    bump: int

class SnapshotResponse(BaseModel):
    listings: List[SnapshotListing]
    appid: Optional[int]
    sku: Optional[str]
    createdAt: Optional[int]