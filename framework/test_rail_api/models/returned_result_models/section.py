from framework.test_rail_api.base.base_returned_model import BaseReturnedModel


class Section(BaseReturnedModel):
    def __init__(self, response_body):
        super().__init__(response_body)
