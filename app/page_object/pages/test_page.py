from selenium.webdriver.common.by import By

from framework.elements.label import Label
from framework.elements.link import Link
from framework.utils.regex_utils import fetch_by_regex_group


class TestPage:
    def __init__(self):
        self.__test_name = Label(By.XPATH, "//h4[text()='Test name']//following-sibling::p", "Test name")
        self.__test_method = Label(By.XPATH, "//h4[text()='Test method name']//following-sibling::p", "Test method")
        self.__test_status = Label(By.XPATH, "//h4[text()='Status']//following-sibling::p//span", "Test status")
        self.__time_start = Label(By.XPATH,
                                  "//h4[text()='Time info']//following-sibling::p[contains(text(),'Start time')]",
                                  "Test start time")
        self.__time_end = Label(By.XPATH, "//h4[text()='Time info']//following-sibling::p[contains(text(),'End time')]",
                                "Test end time")
        self.__test_environment = Label(By.XPATH, "//h4[text()='Environment']//following-sibling::p",
                                        "Test environment")
        self.__test_browser = Label(By.XPATH, "//h4[text()='Browser']//following-sibling::p", "Test browser")
        self.__test_attachment = Link(By.XPATH, "//th[text()='Attachment']//..//following-sibling::tr//a",
                                      "Test attachment")

    @property
    def test_name(self) -> str:
        return self.__test_name.get_text()

    @property
    def test_method(self) -> str:
        return self.__test_method.get_text()

    @property
    def test_status(self) -> str:
        return self.__test_status.get_text().upper()

    @property
    def time_start(self) -> str:
        return fetch_by_regex_group("Start time: (.+)", self.__time_start.get_text(), 1)

    @property
    def time_end(self) -> str:
        return fetch_by_regex_group("End time: (.+)", self.__time_end.get_text(), 1)

    @property
    def test_environment(self) -> str:
        return self.__test_environment.get_text()

    @property
    def test_browser(self) -> str:
        return self.__test_browser.get_text()

    @property
    def link_to_test_attachment(self) -> str:
        return self.__test_attachment.href.split(',')[1]
