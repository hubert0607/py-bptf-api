from typing import Optional, List
from pydantic import BaseModel

class EntityV2(BaseModel):
    id: int
    name: Optional[str] = None
    color: Optional[str] = None

class targetItem(BaseModel):
    itemName: str

class Recipe(BaseModel):
    targetItem: targetItem

class Spell(BaseModel):
    id: Optional[str] = None
    spellId: str
    name: Optional[str] = None
    type: str

class ItemV2(BaseModel):
    baseName: str
    quantity: Optional[int] = None
    quality: Optional[EntityV2] = None
    paint: Optional[EntityV2] = None
    particle: Optional[EntityV2] = None
    elevatedQuality: Optional[EntityV2] = None

    tradable: bool
    craftable: bool

    killstreakTier: Optional[int] = None
    sheen: Optional[EntityV2] = None
    killstreaker: Optional[EntityV2] = None

    recipe: Optional[Recipe] = None

    festivized: Optional[bool] = None
    australium: Optional[bool] = None

    spells: Optional[List[Spell]] = None

class ListingCurrencies(BaseModel):
    metal: Optional[float] = None
    keys: Optional[float] = None

class ListingResolvable(BaseModel):
    id: Optional[int] = None
    item: Optional[ItemV2] = None
    offers: int
    buyout: int
    details: Optional[str] = None
    currencies: ListingCurrencies
