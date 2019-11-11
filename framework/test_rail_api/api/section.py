from framework.test_rail_api.base.base_api import BaseApi

from framework.test_rail_api.models.returned_result_models.section import Section as SectionResponse
from resources import config


class Section(BaseApi):
    METHOD_ADD = "add_section"
    METHOD_GET = "get_section"
    METHOD_DELETE = "delete_section"

    def __init__(self, login, password):
        super().__init__(login, password)

    def add(self, name, suite_id):
        data = {
            "name": name,
            "suite_id": suite_id}
        return SectionResponse(
            self.post_request(Section.METHOD_ADD, config.PROJECT_NUMBER, data).json())

    def get(self, section_id):
        return SectionResponse(
            self.get_request(Section.METHOD_GET, section_id).json())

    def delete(self, section_id):
        self.post_request(Section.METHOD_DELETE, section_id)
