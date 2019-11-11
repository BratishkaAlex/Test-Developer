from framework.utils.comparison_utils import are_images_equal


class Test:
    def __init__(self, name: str, status: str, method: str, start_time: str, end_time: str, environment: str,
                 browser: str, attachment):
        self.__name = name
        self.__status = status
        self.__method = method
        self.__start_time = start_time
        self.__end_time = end_time
        self.__environment = environment
        self.__browser = browser
        self.__attachment = attachment

    @property
    def name(self):
        return self.__name

    @property
    def status(self):
        return self.__status

    @property
    def method(self):
        return self.__method

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
        return self.__end_time

    @property
    def environment(self):
        return self.__environment

    @property
    def browser(self):
        return self.__browser

    @property
    def attachment(self):
        return self.__attachment

    def __eq__(self, other):
        if not isinstance(other, Test):
            return NotImplemented
        return self.name == other.name and self.status == other.status and self.method == other.method \
               and self.start_time == other.start_time and self.end_time == other.end_time and self.environment == \
               other.environment and self.browser == other.browser \
               and are_images_equal(self.attachment, other.attachment)
