from selenium.webdriver.common.by import By

from framework.base.base_page import BasePage
from framework.elements.button import Button
from framework.elements.input_field import InputField
from framework.elements.label import Label


class AddProjectPage(BasePage):
    def __init__(self):
        super().__init__(By.ID, "addProjectForm")
        self.__input_project_name_field = InputField(By.ID, "projectName", "Enter project name")
        self.__save_project_button = Button(By.XPATH, "//button[@type='submit']", "Save project")

    def input_project_name(self, project_name: str):
        self.__input_project_name_field.send_keys(project_name)

    def save_project(self):
        self.__save_project_button.click()

    def is_project_saved(self, project_name: str) -> bool:
        return self.get_success_project_save_message(project_name).is_displayed()

    def get_success_project_save_message(self, project_name: str) -> Label:
        return Label(By.XPATH,
                     f"//div[contains(@class, 'alert-success') and contains(text(), 'Project {project_name} saved')]",
                     "success_project_save_message")
