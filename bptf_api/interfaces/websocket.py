from typing import Optional, List, Union, Dict, Any
from dataclasses import dataclass

@dataclass
class Origin:
    id: int
    name: str

@dataclass
class Quality:
    id: int
    name: str
    color: str

@dataclass
class Spell:
    id: str
    spellId: str
    name: str
    type: str
    defindex: Optional[int] = None
    color: Optional[str] = None

@dataclass
class TextureRarity:
    id: int
    name: str
    color: str

@dataclass
class Texture:
    id: int
    itemDefindex: int
    rarity: TextureRarity
    name: str

@dataclass
class WearTier:
    id: int
    name: str
    short: str

@dataclass
class KillEaterScoreKillEater:
    name: str

@dataclass
class KillEaterScore:
    score: int
    killEater: KillEaterScoreKillEater

@dataclass
class Particle:
    id: int
    name: str
    shortName: str
    imageUrl: str
    type: str

@dataclass
class Sheen:
    id: int
    name: str

@dataclass
class Killstreaker:
    id: int
    name: str

@dataclass
class Paint:
    id: int
    name: str
    color: str

@dataclass
class StrangePartKillEater:
    id: int
    name: str
    item: 'Item'

@dataclass
class StrangePart:
    score: int
    killEater: StrangePartKillEater

@dataclass
class Recipe:
    estimatedCraftingCost: List[Any]
    inputItems: List[Any]
    targetItem: 'TargetItem'
    outputItem: Optional[Any] = None

@dataclass
class TargetItemSource:
    _id: str
    name: str
    defindex: int
    item_class: str
    item_type_name: str
    item_name: str
    proper_name: bool
    item_slot: str
    item_quality: int
    image_inventory: str
    min_ilevel: int
    max_ilevel: int
    image_url: str
    image_url_large: str
    craft_class: str
    craft_material_type: str
    capabilities: Dict[str, bool]
    styles: List[Dict[str, str]]
    used_by_classes: List[str]
    first_sale_date: int
    release_date: int
    appid: int
    _keywords: List[str]

@dataclass
class TargetItem:
    itemName: str
    imageUrl: str
    _source: TargetItemSource

@dataclass
class ItemPriceEntry:
    raw: int
    short: str
    long: str
    usd: Optional[float] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    valueHigh: Optional[float] = None
    updatedAt: Optional[int] = None
    difference: Optional[float] = None

@dataclass
class ItemPrice:
    steam: Optional[ItemPriceEntry] = None
    suggested: Optional[ItemPriceEntry] = None
    community: Optional[ItemPriceEntry] = None

@dataclass
class Item:
    appid: int
    baseName: str
    defindex: int
    id: str
    imageUrl: str
    marketName: str
    name: str
    quality: Quality
    summary: str
    price: Union[ItemPrice, List[ItemPrice]]
    tradable: bool
    craftable: bool
    originalId: str
    origin: Optional[Origin] = None
    class_: Optional[List[str]] = None
    slot: Optional[str] = None
    level: Optional[int] = None
    customDesc: Optional[str] = None
    tag: Optional[str] = None
    spells: Optional[List[Spell]] = None
    elevatedQuality: Optional[Quality] = None
    texture: Optional[Texture] = None
    wearTier: Optional[WearTier] = None
    killEaters: Optional[List[KillEaterScore]] = None
    particle: Optional[Particle] = None
    sheen: Optional[Sheen] = None
    killstreaker: Optional[Killstreaker] = None
    paint: Optional[Paint] = None
    festivized: Optional[bool] = None
    australium: Optional[bool] = None
    strangeParts: Optional[List[StrangePart]] = None
    recipe: Optional[Recipe] = None
    priceindex: Optional[str] = None

@dataclass
class User:
    id: str
    name: str
    avatar: str
    avatarFull: str
    premium: bool
    online: bool
    banned: bool
    customNameStyle: str
    acceptedSuggestions: int
    class_: str
    style: str
    tradeOfferUrl: str
    isMarketplaceSeller: bool
    bans: List[Any]
    role: Optional[str] = None
    flagImpersonated: Optional[str] = None

@dataclass
class PayloadValue:
    raw: int
    short: str
    long: str

@dataclass
class PayloadCurrencies:
    metal: Optional[float] = None
    keys: Optional[float] = None

@dataclass
class Payload:
    id: str
    steamid: str
    appid: int
    currencies: PayloadCurrencies
    value: PayloadValue
    listedAt: int
    bumpedAt: int
    intent: str
    count: int
    status: str
    source: str
    item: Item
    user: User
    details: Optional[str] = None
    tradeOffersPreferred: Optional[bool] = None
    buyoutOnly: Optional[bool] = None

@dataclass
class EventMessage:
    id: str
    event: str
    payload: Payload