from enum import IntEnum
from pydantic import BaseModel, ConfigDict, SerializeAsAny
from typing import Optional

class Intent(IntEnum):
    BUY = 0
    SELL = 1

class Currencies(BaseModel):
    metal: float = 0
    keys: int = 0

class ItemV1(BaseModel):
    quality: str = 'Unique'
    item_name: str 
    craftable: int = 1
    priceindex: int = 0

    elevated_quality: str = None
    particle_name: str = None

    model_config = ConfigDict(exclude={"elevated_quality", "particle_name"})

    def model_dump(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)

        data["item_name"] = data["item_name"].replace(self.quality + " ", '')

        if self.elevated_quality:
            data["item_name"] = data["item_name"].replace(self.elevated_quality + " ", '')
            data["quality"] = f"{self.elevated_quality} {self.quality}"

        if self.particle_name:
            data["item_name"] = data["item_name"].replace(self.particle_name + " ", '')

        if self.priceindex != 0 and self.particle_name is None:
            raise ValueError('You forgot to set up particle_name')

        if self.priceindex == 0 and self.particle_name is not None:
            raise ValueError('You forgot to set up priceindex (id of particle name)')

        if self.craftable == 0:
            data["item_name"] = data["item_name"].replace('Non-Craftable ', '')
        return data




class ListingV1(BaseModel):
    intent: Intent
    id: Optional[str] = None
    offers: int = 1
    buyout: int = 1
    promoted: int = 0
    details: str = ""
    currencies: Currencies
    item: SerializeAsAny[ItemV1]

    model_config = ConfigDict(use_enum_values=True)

    def model_dump(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)
        data["item"] = self.item.model_dump(*args, **kwargs)
        return data


if __name__ == '__main__':
    listing = ListingV1(
        intent=Intent.BUY,
        details='test',
        currencies=Currencies(metal=8.11),
        item=ItemV1(item_name='Strange Specialized Killstreak Australium Sniper Rifle', quality='Strange')
    )


    print(listing.model_dump())