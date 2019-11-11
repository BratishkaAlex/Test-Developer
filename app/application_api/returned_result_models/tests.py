class Tests:
    def __init__(self, parsed_xml_string):
        if "<test>" not in parsed_xml_string:
            raise ValueError("Wrong format of api response")
        self.__response_body = f"<rich-text>{parsed_xml_string}</rich-text>"

    @property
    def response_body(self):
        return self.__response_body
