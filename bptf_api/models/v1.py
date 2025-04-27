from enum import IntEnum
from pydantic import BaseModel, ConfigDict
from typing import Optional

class Intent(IntEnum):
    BUY = 0
    SELL = 1

class Currencies(BaseModel):
    metal: float = 0
    keys: int = 0



class ItemV1(BaseModel):
    quality: int = 6
    item_name: str
    craftable: int = 1
    priceindex: int = 0

class ListingV1(BaseModel):
    intent: Intent
    id: Optional[str] = None
    offers: int = 1
    buyout: int = 1
    promoted: int = 0
    details: str = ""
    currencies: Currencies
    item: Optional[ItemV1] = None

    model_config = ConfigDict(use_enum_values=True)

