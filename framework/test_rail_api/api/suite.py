from framework.test_rail_api.base.base_api import BaseApi
from framework.test_rail_api.models.returned_result_models.suite import Suite as SuiteResponse
from resources import config


class Suite(BaseApi):
    METHOD_ADD = "add_suite"
    METHOD_GET = "get_suite"
    METHOD_DELETE = "delete_suite"

    def __init__(self, login, password):
        super().__init__(login, password)

    def add(self, name, description):
        data = {
            "name": name,
            "description": description
        }
        return SuiteResponse(self.post_request(Suite.METHOD_ADD, config.PROJECT_NUMBER,
                                               data).json())

    def get(self, suite_id):
        return SuiteResponse(self.get_request(Suite.METHOD_GET, suite_id).json())

    def delete(self, suite_id):
        self.post_request(Suite.METHOD_DELETE, suite_id)
