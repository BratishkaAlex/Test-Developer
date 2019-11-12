import random

from framework.test_rail_api.base.base_api import BaseApi
from framework.test_rail_api.constants.case_statuses import CaseStatuses
from framework.test_rail_api.models.returned_result_models.case import Case as CaseResponse


class Case(BaseApi):
    METHOD_ADD = "add_case"
    METHOD_GET = "get_case"
    METHOD_DELETE = "delete_case"
    METHOD_ADD_RESULT = "add_result_for_case"

    def __init__(self, login, password):
        super().__init__(login, password)

    def add(self, name, section_id):
        data = {
            "title": name,
            "template_id": 1
        }
        return CaseResponse(
            self.post_request(Case.METHOD_ADD, section_id, data).json())

    def get(self, case_id):
        return CaseResponse(self.get_request(Case.METHOD_GET, case_id).json())

    def add_result(self, run_id: int, case_id: int, comment: str):
        data = {
            "comment": comment
        }
        self.post_request(Case.METHOD_ADD_RESULT, f"{run_id}/{case_id}", data)

    def delete(self, case_id):
        self.post_request(Case.METHOD_DELETE, case_id)

    @staticmethod
    def get_random_status():
        allowed_case_statuses = [CaseStatuses.PASSED.value, CaseStatuses.BLOCKED.value, CaseStatuses.RETEST.value,
                                 CaseStatuses.FAILED.value]
        return allowed_case_statuses[random.randint(0, len(allowed_case_statuses) - 1)]
