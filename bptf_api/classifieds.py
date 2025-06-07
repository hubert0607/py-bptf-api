import requests
import os
from ratelimit import limits, sleep_and_retry
import logging

from models import ListingPatchRequest, SnapshotResponse, ListingResolvable, ListingCurrencies, ItemV2

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


BATCH_OPERATION_LIMIT = 10          #per minute
STANDARD_CLASSIFIEDS_LIMIT = 60     #per minute 


class Classifieds:

    def __init__(self):
        self.token = os.getenv('BP_TOKEN')
        if self.token is None or self.token == "":
            raise ValueError("No token found in environment variables")
            

    @sleep_and_retry
    @limits(calls=STANDARD_CLASSIFIEDS_LIMIT, period=60)
    def update_listing(self, listing_id: str, update_model: ListingPatchRequest):
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


class BatchClientV2:
    def __init__(self):
        self.token = os.getenv('BP_TOKEN')
        if self.token is None or self.token == "":
            raise ValueError("No token found in environment variables")
        self.listings = []
            
    def _add_listing(self, listing: ListingResolvable) -> None:
        """Add a listing to the batch and check if batch should be sent"""
        self.listings.append(listing)
        if len(self.listings) >= 100:
            self.send_batch()
    
    def add_buy_listing(self, item: ItemV2, currencies: ListingCurrencies, details: str = None) -> None:
        """Add a buy listing to the batch"""
        listing = ListingResolvable(
            item=item,
            currencies=currencies,
            offers=1,
            buyout=1,
            details=details
        )
        self._add_listing(listing)
    
    def add_sell_listing(self, item_id: int, currencies: ListingCurrencies, details: str = None) -> None:
        """Add a sell listing to the batch"""
        listing = ListingResolvable(
            id=item_id,
            offers=1,
            buyout=1,
            currencies=currencies,
            details=details
        )
        self._add_listing(listing)
    
    @sleep_and_retry
    @limits(calls=BATCH_OPERATION_LIMIT, period=60)
    def send_batch(self):
        if len(self.listings) == 0:
            return

        batch_to_send = self.listings.copy()
        self.listings = []
        
        url = 'https://backpack.tf/api/v2/classifieds/listings/batch'
        params = {"token": self.token}
        
        response = requests.post(
            url, 
            json=[listing.model_dump(exclude_none=True) for listing in batch_to_send], 
            params=params
        )
        response.raise_for_status()
        return response.json()

               

if __name__ == "__main__":
    c = Classifieds()
    
    # snapshot = c.get_snapshot("The Liberty Launcher")
    # print(snapshot)
    
    # Example of using BatchClientV2 synchronously
    # client = BatchClientV2()
    # # Add listings here...
    # result = client.flush()