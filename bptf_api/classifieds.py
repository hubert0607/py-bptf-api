import requests
import os
from ratelimit import limits, sleep_and_retry
import logging

from interfaces.classifieds import listingPatchRequest


STANDARD_CLASSIFIEDS_LIMIT = 60     #per minute 

class Classifieds:

    def __init__(self):
        self.token = os.getenv('BP_TOKEN')
        if self.token is None or self.token == "":
            raise ValueError("No token found in environment variables")
            

    @sleep_and_retry
    @limits(calls=STANDARD_CLASSIFIEDS_LIMIT, period=60)
    def update_listing(self, listing_id: str, update_model: listingPatchRequest):
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