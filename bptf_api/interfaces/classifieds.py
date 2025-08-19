from typing import Optional
from pydantic import BaseModel

class ListingCurrencies(BaseModel):
    metal: Optional[float] = None
    keys: Optional[float] = None

class ListingPatchRequest(BaseModel):
    currencies: ListingCurrencies
    details: Optional[str] = None
    quantity: Optional[int] = None
