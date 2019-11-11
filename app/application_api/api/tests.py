from app.application_api.base_application_api import BaseApplicationApi
from app.application_api.returned_result_models.tests import Tests as TestsResponse


class Tests(BaseApplicationApi):
    METHOD_GET_LIST_XML = "/test/get/xml"

    def get_tests(self, project_id: int) -> TestsResponse:
        data = {
            "projectId": str(project_id)
        }
        return TestsResponse(self.post_request(self.METHOD_GET_LIST_XML, data).text)
