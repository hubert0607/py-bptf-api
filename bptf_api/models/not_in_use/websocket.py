# from typing import List, Optional
# from pydantic import BaseModel


# class Quality(BaseModel):
#     id: int
#     name: str


# class Particle(BaseModel):
#     id: int
#     name: str


# class Spells(BaseModel):
#     id: str
#     spellId: str
#     name: str
#     type: str


# class Sheen(BaseModel):
#     id: int
#     name: str


# class Killstreaker(BaseModel):
#     id: int
#     name: str


# class ElevatedQuality(BaseModel):
#     id: int
#     name: str


# class Texture(BaseModel):
#     id: int
#     itemDefindex: int
#     name: str


# class WearTier(BaseModel):
#     id: int
#     name: str


# # Forward reference for nested KillEater -> Item reference
# class Item(BaseModel):
#     pass


# class KillEater(BaseModel):
#     item: Item


# class StrangeParts(BaseModel):
#     killEater: KillEater


# class Item(BaseModel):
#     defindex: int
#     name: str
#     quality: Quality
#     elevatedQuality: ElevatedQuality
#     slot: str
#     particle: Particle
#     tradable: bool
#     craftable: bool
#     australium: bool
#     festivized: bool
#     killstreakTier: int
#     sheen: Sheen
#     killstreaker: Killstreaker
#     texture: Texture
#     wearTier: WearTier
#     spells: List[Spells]
#     strangeParts: List[StrangeParts]


# class Currencies(BaseModel):
#     metal: float
#     keys: int
#     usd: float


# class UserAgent(BaseModel):
#     client: str
#     lastPulse: int


# class User(BaseModel):
#     id: str
#     name: str
#     premium: bool
#     banned: bool
#     # Using Python's alternative for the 'class' keyword
#     class_: str = None
#     style: str
#     role: Optional[str] = None
#     tradeOfferUrl: str
#     bans: List[str]

#     # This model configuration makes 'class' in JSON map to 'class_' in Python
#     class Config:
#         fields = {'class_': 'class'}


# class Payload(BaseModel):
#     id: str
#     steamid: str
#     offers: str
#     buyout: str
#     appid: int
#     currencies: Currencies
#     details: str
#     listedAt: int
#     bumpedAt: int
#     intent: str
#     status: str
#     source: str
#     userAgent: UserAgent
#     user: User
#     item: Item


# class EventMessage(BaseModel):
#     id: str
#     event: str
#     payload: Payload