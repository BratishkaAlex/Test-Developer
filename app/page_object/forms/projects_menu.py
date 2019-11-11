from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.link import Link
from framework.utils.regex_utils import fetch_by_regex_group


class ProjectsMenu:
    def __init__(self):
        self.__add_project_button = Button(By.CSS_SELECTOR, ".btn-xs", "Add project")

    def get_menu_item(self, project_name: str) -> Link:
        return Link(By.XPATH, f"//a[@class='list-group-item' and text()='{project_name}']",
                    f"navigate to project {project_name}")

    def get_project_id(self, project_name: str) -> int:
        return int(fetch_by_regex_group("projectId=(\\d+)", self.get_menu_item(project_name).href, 1))

    def navigate_to(self, project_name: str):
        self.get_menu_item(project_name).click()

    def add_project(self):
        self.__add_project_button.click()

    def is_project_displayed(self, project_name: str) -> bool:
        return self.get_menu_item(project_name).is_displayed()
