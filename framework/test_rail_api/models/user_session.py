from framework.test_rail_api.api.case import Case
from framework.test_rail_api.api.run import Run
from framework.test_rail_api.api.section import Section
from framework.test_rail_api.api.suite import Suite


class UserSession:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.suite = Suite(self.__login, self.__password)
        self.section = Section(self.__login, self.__password)
        self.case = Case(self.__login, self.__password)
        self.run = Run(self.__login, self.__password)
