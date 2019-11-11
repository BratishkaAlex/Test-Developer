from logging import info

from selenium.webdriver.common.alert import Alert

from framework.browser.browser import Browser


class ModalWindow:
    def __init__(self):
        self.__alert_driver = Alert(Browser().driver)

    @property
    def alert_driver(self):
        return self.__alert_driver

    def get_text(self):
        info("Checking modal window message")
        return self.alert_driver.text

    def accept(self):
        info("Accept modal window message")
        self.alert_driver.accept()

    def send_keys(self, text):
        info("Send keys to modal window")
        self.alert_driver.send_keys(text)
