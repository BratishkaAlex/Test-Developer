from selenium.webdriver.common.by import By

from app.page_object.forms.projects_menu import ProjectsMenu
from framework.base.base_page import BasePage
from resources import config


class AllProjectsPage(BasePage):
    def __init__(self):
        super().__init__(By.XPATH, f"//footer//span[text()='Version: {config.VARIANT}']")
        self.__projects_menu = ProjectsMenu()

    @property
    def projects_menu(self) -> ProjectsMenu:
        return self.__projects_menu
