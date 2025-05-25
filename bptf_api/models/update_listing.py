from pydantic import BaseModel
from typing import Optional

class Currencies(BaseModel):
    metal: Optional[float] = 0
    keys: Optional[int] = 0

class UpdateListingV2(BaseModel):
    currencies: Currencies
    details: str = ""
    quantity: Optional[int] = 1