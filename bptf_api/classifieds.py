import requests
import os
from ratelimit import limits, sleep_and_retry
import logging

from models.batch import ListingV1
from models.snapshot import SnapshotResponse
from models.update_listing import UpdateListingV2

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


BATCH_OPERATION_LIMIT = 10          #per minute
STANDARD_CLASSIFIEDS_LIMIT = 60     #per minute 


class BatchRequest():
    
    def __init__(self, token):
        self.token = token
        self.batch_listings: list[dict] = []

        
    def add_listing_to_batch(self, listing: ListingV1) -> None:
        self.batch_listings.append(listing.model_dump(exclude_none=True))

    @sleep_and_retry
    @limits(calls=BATCH_OPERATION_LIMIT, period=60)
    def create_listings_batch(self) -> None:
        url = "https://backpack.tf/api/classifieds/list/v1"
        
        payload = {
            "token": self.token,
            "listings": self.batch_listings
        }

        try:
            response = requests.post(url, json=payload)
            print(response.json())

            self.batch_listings = []
        except requests.HTTPError as e:
            logging.error(f"Error creating batch listings: {e}")    



class Classifieds:

    def __init__(self):
        self.token = os.getenv('BP_TOKEN')
        if self.token is None or self.token == "":
            raise ValueError("No token found in environment variables")
            

    def prepare_batch(self) -> BatchRequest:
        return BatchRequest(self.token)


    @sleep_and_retry
    @limits(calls=STANDARD_CLASSIFIEDS_LIMIT, period=60)
    def update_listing(self, listing_id: str, update_model: UpdateListingV2):
        url = f"https://backpack.tf/api/v2/classifieds/listings/{listing_id}"

        params = {
            "token": self.token
        }
        payload = update_model.model_dump(exclude_none=True)
        response = requests.patch(url, json=payload, params=params)

        try:
            response.raise_for_status()
            return response.json() 

        except requests.HTTPError as e:
            logging.error(f"Error updating listing: {e} \nResponse: {response.json()}")
            return response.json()


    @sleep_and_retry
    @limits(calls=STANDARD_CLASSIFIEDS_LIMIT, period=60)
    def delete_listing(self, listing_id: str) -> bool:
        url = f"https://backpack.tf/api/v2/classifieds/listings/{listing_id}"

        params = {
            "token": self.token
        }

        response = requests.delete(url, params=params)

        try:
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            logging.error(f"Error deleting listing: {e} \nResponse: {response.json()}")
            return response.json()


    @sleep_and_retry
    @limits(calls=STANDARD_CLASSIFIEDS_LIMIT, period=60)
    def get_snapshot(self, name: str) -> SnapshotResponse:
        url = "https://backpack.tf/api/classifieds/listings/snapshot"

        params = {
            "token": self.token,
            "appid": 440,
            "sku": name
        }

        response = requests.get(url, params=params)
        try:
            response.raise_for_status()
            response_json = response.json()
            print(response.json())
            return SnapshotResponse(**response_json)
        except requests.HTTPError as e:
            logging.error(f"Error taking snapshot: {e} \nResponse: {response.json()}")





if __name__ == "__main__":
    c = Classifieds()
    
    # snapshot = c.get_snapshot("The Liberty Launcher")
    # print(snapshot)

    from models.batch import Intent, Currencies, ItemV1
    batch = c.prepare_batch()
    listing = ListingV1(
        intent=Intent.BUY,
        details='test',
        currencies=Currencies(metal=12.11),
        item=ItemV1(item_name='Strange Hot Professional Killstreak Minigun', quality='Strange', particle_name="Hot", priceindex=701)
        # item=ItemV1(item_name='Professional Killstreak Phlogistinator Kit', quality='Unique', craftable=0)
        # item=ItemV1(item_name="Non-Craftable Conjurer's Cowl", quality='Unique', craftable=0)
    )
    print(listing.model_dump())
    batch.add_listing_to_batch(listing)
    batch.create_listings_batch()