import os
import requests
from ratelimit import limits, sleep_and_retry
import logging

from .interfaces.snapshots import SnapshotResponse

SNAPSHOT_OPERATION_LIMIT = 60     #per minute

class SnapshotClient:
    def __init__(self):
        self.token = os.getenv('BP_TOKEN')
        if self.token is None or self.token == "":
            raise ValueError("No token found in environment variables")

    @sleep_and_retry
    @limits(calls=SNAPSHOT_OPERATION_LIMIT, period=60)
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