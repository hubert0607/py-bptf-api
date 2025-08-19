from dataclasses import dataclass
from typing import Optional

@dataclass
class ListingCurrencies:
    metal: Optional[float] = None
    keys: Optional[float] = None

@dataclass
class ListingPatchRequest:
    currencies: ListingCurrencies
    details: Optional[str] = None
    quantity: Optional[int] = None