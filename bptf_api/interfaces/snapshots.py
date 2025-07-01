from typing import Optional, List, Union
from pydantic import BaseModel

class Attribute(BaseModel):
    defindex: int
    value: Optional[Union[str, float, int, None]] = None
    float_value: Optional[float] = None

class Item(BaseModel):
    id: Optional[int] = None
    original_id: Optional[int] = None
    defindex: int
    quality: int
    quantity: Optional[Union[int, str]] = None
    attributes: Optional[List[Attribute]] = None
    marketplace_price: Optional[float] = None
    marketplace_sku: Optional[str] = None

class SnapshotCurrencies(BaseModel):
    usd: Optional[float] = None
    keys: Optional[float] = None
    metal: Optional[float] = None

class SnapshotListing(BaseModel):
    steamid: str
    offers: int
    buyout: int
    details: str
    intent: str
    timestamp: int
    price: float
    item: Item
    currencies: SnapshotCurrencies
    bump: int

class SnapshotResponse(BaseModel):
    listings: List[SnapshotListing]
    appid: Optional[int] = None
    sku: Optional[str] = None
    created_at: Optional[int] = None
