from dataclasses import dataclass
from typing import Optional, List

@dataclass
class EntityV2:
    id: int
    name: Optional[str] = None
    color: Optional[str] = None

@dataclass
class TargetItem:
    itemName: str

@dataclass
class Recipe:
    targetItem: TargetItem

@dataclass
class Spell:
    spellId: str
    type: str
    id: Optional[str] = None
    name: Optional[str] = None

@dataclass
class ItemV2:
    baseName: str
    tradable: bool
    craftable: bool
    quantity: Optional[int] = None
    quality: Optional[EntityV2] = None
    paint: Optional[EntityV2] = None
    particle: Optional[EntityV2] = None
    elevatedQuality: Optional[EntityV2] = None
    killstreakTier: Optional[int] = None
    sheen: Optional[EntityV2] = None
    killstreaker: Optional[EntityV2] = None
    recipe: Optional[Recipe] = None
    festivized: Optional[bool] = None
    australium: Optional[bool] = None
    spells: Optional[List[Spell]] = None

@dataclass
class ListingCurrencies:
    metal: Optional[float] = None
    keys: Optional[float] = None

@dataclass
class ListingResolvable:
    offers: int
    buyout: int
    currencies: ListingCurrencies
    id: Optional[int] = None
    item: Optional[ItemV2] = None
    details: Optional[str] = None