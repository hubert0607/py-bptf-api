from typing import Optional, List, Union, Dict, Any
from pydantic import BaseModel

class Origin(BaseModel):
    id: int
    name: str

class Quality(BaseModel):
    id: int
    name: str
    color: str

class Spell(BaseModel):
    id: str
    spellId: str
    name: str
    type: str
    defindex: Optional[int] = None
    color: Optional[str] = None

class TextureRarity(BaseModel):
    id: int
    name: str
    color: str

class Texture(BaseModel):
    id: int
    itemDefindex: int
    rarity: TextureRarity
    name: str

class WearTier(BaseModel):
    id: int
    name: str
    short: str

class KillEaterScoreKillEater(BaseModel):
    name: str

class KillEaterScore(BaseModel):
    score: int
    killEater: KillEaterScoreKillEater

class Particle(BaseModel):
    id: int
    name: str
    shortName: str
    imageUrl: str
    type: str

class Sheen(BaseModel):
    id: int
    name: str

class Killstreaker(BaseModel):
    id: int
    name: str

class Paint(BaseModel):
    id: int
    name: str
    color: str

class StrangePartKillEater(BaseModel):
    id: int
    name: str
    item: 'Item'

class StrangePart(BaseModel):
    score: int
    killEater: StrangePartKillEater

class Recipe(BaseModel):
    estimatedCraftingCost: List[Any]
    inputItems: List[Any]
    outputItem: Optional[Any] = None
    targetItem: 'TargetItem'

class TargetItemSource(BaseModel):
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

class TargetItem(BaseModel):
    itemName: str
    imageUrl: str
    _source: TargetItemSource

class ItemPriceEntry(BaseModel):
    raw: int
    short: str
    long: str
    usd: Optional[float] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    valueHigh: Optional[float] = None
    updatedAt: Optional[int] = None
    difference: Optional[float] = None

class ItemPrice(BaseModel):
    steam: Optional[ItemPriceEntry] = None
    suggested: Optional[ItemPriceEntry] = None
    community: Optional[ItemPriceEntry] = None

class Item(BaseModel):
    appid: int
    baseName: str
    defindex: int
    id: str
    imageUrl: str
    marketName: str
    name: str
    origin: Optional[Origin] = None
    originalId: str
    quality: Quality
    summary: str
    price: Union[ItemPrice, List[ItemPrice]]
    class_: Optional[List[str]] = None
    slot: Optional[str] = None
    tradable: bool
    craftable: bool
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

    class Config:
        fields = {'class_': 'class'}

class User(BaseModel):
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
    role: Optional[str] = None
    tradeOfferUrl: str
    isMarketplaceSeller: bool
    flagImpersonated: Optional[str] = None
    bans: List[Any]

    class Config:
        fields = {'class_': 'class'}

class PayloadValue(BaseModel):
    raw: int
    short: str
    long: str

class PayloadCurrencies(BaseModel):
    metal: Optional[float] = None
    keys: Optional[float] = None

class Payload(BaseModel):
    id: str
    steamid: str
    appid: int
    currencies: PayloadCurrencies
    value: PayloadValue
    details: Optional[str] = None
    listedAt: int
    bumpedAt: int
    intent: str
    count: int
    status: str
    source: str
    tradeOffersPreferred: Optional[bool] = None
    buyoutOnly: Optional[bool] = None
    item: Item
    user: User

class EventMessage(BaseModel):
    id: str
    event: str
    payload: Payload
