from app.application_api.base_application_api import BaseApplicationApi
from resources import config


class Token(BaseApplicationApi):
    METHOD_GET = "token/get"

    def get(self) -> str:
        data = {
            "variant": f"{config.VARIANT}"
        }
        return self.post_request(self.METHOD_GET, data).text
