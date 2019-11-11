import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from framework.browser.browser_factory import get_driver, get_remote_driver
from framework.models.cookie import Cookie
from framework.models.singleton import Singleton
from framework.utils.logger import debug
from resources import config


class Browser(metaclass=Singleton):
    def __init__(self):
        browser_name = config.BROWSER
        if "BROWSER" in os.environ:
            browser_name = os.environ["BROWSER"]
        self.__driver = get_driver(browser_name)

    @property
    def driver(self) -> webdriver:
        return self.__driver

    def maximize(self):
        debug("Maximize browser window")
        self.driver.maximize_window()

    def enter_url(self, url: str):
        debug(f"Entering {url}")
        self.driver.get(url)

    def close_tab(self):
        debug("Close tab")
        self.driver.close()

    def get_current_url(self) -> str:
        debug("Get current browser")
        return self.driver.current_url

    def get_elements_list(self, locator_type: By, locator: str) -> list:
        return self.driver.find_elements(locator_type, locator)

    def refresh_page(self):
        self.driver.refresh()

    def set_implicitly_wait(self, timeout: int):
        self.driver.implicitly_wait(timeout)

    def add_cookie(self, cookie: Cookie):
        self.driver.add_cookie({"name": cookie.name, "value": cookie.value})

    def delete_cookie(self, cookie: Cookie):
        self.driver.delete_cookie(cookie.name)

    def are_cookies_exist(self, cookie_list: list) -> bool:
        for cookie in cookie_list:
            if not self.is_cookie_exist(cookie):
                return False
        return True

    def is_cookie_exist(self, cookie: Cookie) -> bool:
        return self.driver.get_cookie(cookie.name) is not None

    def back(self):
        self.driver.back()

    def switch_to_window(self, window_number: int):
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def save_screenshot(self, path_to_save_screenshot: str):
        debug("Make screenshot")
        self.driver.get_screenshot_as_file(path_to_save_screenshot)

    def click_by_coordinates(self, x: int, y: int):
        action = webdriver.ActionChains(self.driver)
        action.move_by_offset(x, y).click().perform()
