import json

import requests

from framework.utils.logger import debug
from resources import config


class BaseApi:
    DEFAULT_HEADER = {"Content-Type": "application/json"}

    def __init__(self, login, password):
        self.__auth = (login, password)
        self.__base_url = f"{config.TEST_RAIL_URL}/{config.TEST_RAIL_API_URL}"

    def post_request(self, method, parameters, data=None):
        debug("Performing post request")
        return requests.post(f"{self.__base_url}/{method}/{parameters}", auth=self.__auth,
                             headers=BaseApi.DEFAULT_HEADER, data=json.dumps(data))

    def get_request(self, method, item_id):
        debug("Performing get request")
        return requests.get(f"{self.__base_url}/{method}/{item_id}", auth=self.__auth,
                            headers=BaseApi.DEFAULT_HEADER)
