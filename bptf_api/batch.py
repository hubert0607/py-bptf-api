import os
import requests
from ratelimit import limits, sleep_and_retry

from .interfaces.batch import ListingResolvable, ListingCurrencies, ItemV2

BATCH_OPERATION_LIMIT = 10          #per minute



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