import requests

from framework.utils.logger import debug
from resources import config


class BaseApplicationApi:
    def post_request(self, method: str, data: dict):
        debug("Performing post request")
        return requests.post(f"{config.API_URL}/{method}",
                             data=data)

    def get_request(self, method, item_id):
        debug("Performing get request")
        return requests.get(f"{config.API_URL}/{method}/{item_id}")
