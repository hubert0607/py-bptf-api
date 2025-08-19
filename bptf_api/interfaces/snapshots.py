from dataclasses import dataclass
from typing import Optional, List, Union

@dataclass
class Attribute:
    defindex: int
    value: Optional[Union[str, float, int, None]] = None
    float_value: Optional[float] = None

@dataclass
class Item:
    defindex: int
    quality: int
    id: Optional[int] = None
    original_id: Optional[int] = None
    quantity: Optional[Union[int, str]] = None
    attributes: Optional[List[Attribute]] = None
    marketplace_price: Optional[float] = None
    marketplace_sku: Optional[str] = None

@dataclass
class SnapshotCurrencies:
    usd: Optional[float] = None
    keys: Optional[float] = None
    metal: Optional[float] = None

@dataclass
class SnapshotListing:
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

@dataclass
class SnapshotResponse:
    listings: List[SnapshotListing]
    appid: Optional[int] = None
    sku: Optional[str] = None
    created_at: Optional[int] = None