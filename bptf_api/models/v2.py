from enum import StrEnum
from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from pydantic import field_validator

class IntentV2(StrEnum):
    BUY = 'buy'
    SELL = 'sell'

class Currencies(BaseModel):
    metal: Optional[float] = 0
    keys: Optional[int] = 0
    usd: Optional[float] = 0

    @field_validator('usd')
    def round_usd(cls, v):
        return round(v, 2) if v is not None else v

class Entity(BaseModel):
    name: str
    id: int
    color: Optional[str] = None

class Spell(BaseModel):
    id: str
    spellId: str
    name: str
    type: str
    defindex: Optional[int] = None
    color: Optional[str] = None

class ItemV2(BaseModel):
    baseName: str
    name: str = None
    quantity: Optional[int] = None
    quality: Entity = None
    rarity: Optional[Entity] = None
    paint: Optional[Entity] = None
    particle: Optional[Entity] = None
    elevatedQuality: Optional[Entity] = None
    slot: Optional[str] = None
    wearTier: Optional[Entity] = None
    texture: Optional[Entity] = None
    spells: Optional[List[Spell]] = None
    sheen: Optional[Entity] = None
    killstreaker: Optional[Entity] = None

class ListingV2(BaseModel):
    id: str
    appid: int = 440
    bumpedAt: datetime
    listedAt: datetime
    details: str = ""
    intent: IntentV2
    steamid: str
    buyoutOnly: Optional[bool] = True
    currencies: Currencies
    promoted: Optional[bool] = False
    tradeOffersPreferred: Optional[bool] = True
    count: int = 1
    item: Optional[ItemV2] = None
    model_config = ConfigDict(use_enum_values=True)

class Cursor(BaseModel):
    skip: int
    limit: Optional[int] = None
    total: int

class ScrollableListing(BaseModel):
    results: Optional[list[ListingV2]] = []
    cursor: Cursor

class UpdateListingV2(BaseModel):
    currencies: Currencies
    details: str = ""
    quantity: Optional[int] = 1