import json
from src import config
import requests

class EmailAPI:

    def __init__(self):
        self.base_url = config.EMAIL_API_ENDPOINT
        self.headers = {
            "Content-type": "application/json",
            "Accept": "text/plain"
        }

    def _make_post_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request("POST", url, data=json.dumps(data), headers=self.headers)
        return json.loads(response.text)

    def new_email(self, data, template):
        endpoint = "send_email"
        data['template'] = template
        return self._make_post_request(endpoint, data)
