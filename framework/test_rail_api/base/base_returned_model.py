class BaseReturnedModel:
    def __init__(self, response_body):
        self.__response_body = response_body

    @property
    def id(self):
        if "id" in self.response_body:
            return self.response_body["id"]
        else:
            raise ValueError("There is no such field in response")

    @property
    def response_body(self):
        return self.__response_body

    def __eq__(self, other):
        if not isinstance(other, BaseReturnedModel):
            return NotImplemented
        return self.response_body == other.response_body
