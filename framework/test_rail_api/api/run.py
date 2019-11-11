from framework.test_rail_api.base.base_api import BaseApi
from framework.test_rail_api.models.returned_result_models.run import Run as RunResponse
from resources import config


class Run(BaseApi):
    METHOD_ADD = "add_run"
    METHOD_GET = "get_run"
    METHOD_DELETE = "delete_run"

    def __init__(self, login, password):
        super().__init__(login, password)

    def add(self, name, suite_id):
        data = {
            "name": name,
            "suite_id": suite_id
        }
        return RunResponse(
            self.post_request(Run.METHOD_ADD, config.PROJECT_NUMBER, data).json())

    def get(self, run_id):
        return RunResponse(self.get_request(Run.METHOD_GET, run_id).json())

    def delete(self, run_id):
        self.post_request(Run.METHOD_DELETE, run_id)
