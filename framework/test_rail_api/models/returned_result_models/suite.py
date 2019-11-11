from framework.test_rail_api.base.base_returned_model import BaseReturnedModel


class Suite(BaseReturnedModel):
    def __init__(self, response_body):
        super().__init__(response_body)
