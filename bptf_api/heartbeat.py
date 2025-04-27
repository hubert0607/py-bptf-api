import requests
import os

class Heartbeat:
    def __init__(self):
        self.token = os.getenv('BP_TOKEN')
    def get_status(self):
        url = "https://backpack.tf/api/agent/status"
        params = {
            "token": self.token
        }
        
        response = requests.post(params=params, url=url)
        return response.json()["status"]

    def register_or_refresh(self, user_agent_name):
        url = "https://backpack.tf/api/agent/pulse"
        params = {
            "token": self.token,
        }

        headers = {
            "User-Agent": user_agent_name
        }
        
        response = requests.post(params=params, url=url, headers=headers)
        return response.json()["status"]

    def stop(self):
        url = "https://backpack.tf/api/agent/stop"
        params = {
            "token": self.token
        }
        
        response = requests.post(params=params, url=url)
        return response.json()["status"]

if __name__ == "__main__":
    heartbeat = Heartbeat()
    if heartbeat.get_status() == 'inactive':
        heartbeat.register_or_refresh(user_agent_name="Just say Alohaaaa")

    while heartbeat.stop() != 'inactive':
        continue