from pydantic import BaseModel, field_validator, model_validator
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
    keys: Optional[int] = 0
    metal: Optional[Union[float, int]] = 0

    @field_validator('keys')
    @classmethod
    def validate_keys(cls, v):
        if v is None:
            return v
        if isinstance(v, float):
            if v.is_integer():
                return int(v)
            raise ValueError("Keys must be a whole number")
        return v

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
    appid: Optional[int] = None
    sku: Optional[str] = None
    createdAt: Optional[int] = None

    @model_validator(mode='before')
    @classmethod
    def validate_listings(cls, data):
        if not isinstance(data, dict):
            return data
            
        valid_listings = []
        for listing in data.get('listings', []):
            try:
                valid_listing = SnapshotListing.model_validate(listing)
                valid_listings.append(valid_listing)
            except Exception:
                continue
        
        data['listings'] = valid_listings
        return data