from pydantic import BaseModel
from typing import Optional, List, Union

# For Snapshot method
class Attribute(BaseModel):
    defindex: int
    value: Optional[Union[str, int, None]] = None
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




# For Update Listing method
class ListingCurrencies(BaseModel):
    metal: Optional[float] = None
    keys: Optional[int] = None

class ListingPatchRequest(BaseModel):
    currencies: ListingCurrencies
    details: Optional[str] = None
    quantity: Optional[int] = None




# For Batch methods
class EntityV2(BaseModel):
    id: int
    name: Optional[str] = None
    color: Optional[str] = None

class Spell(BaseModel):
    id: Optional[str] = None
    spellId: str 
    name: Optional[str] = None
    type: str

class ItemV2(BaseModel):
    baseName: str 
    quantity: Optional[int] = None
    quality: Optional[EntityV2] = None
    rarity: Optional[EntityV2] = None
    paint: Optional[EntityV2] = None
    particle: Optional[EntityV2] = None
    elevatedQuality: Optional[EntityV2] = None 

    tradable: bool
    craftable: bool

    killstreakTier: Optional[int] = None 
    sheen: Optional[EntityV2] = None
    killstreaker: Optional[EntityV2] = None

    festivized: Optional[bool] = None
    australium: Optional[bool] = None

    spells: Optional[List[Spell]] = None

class ListingResolvable(BaseModel):
    id: Optional[int] = None
    item: Optional[ItemV2] = None
    offers: int
    buyout: int
    details: Optional[str] = None
    currencies: ListingCurrencies
