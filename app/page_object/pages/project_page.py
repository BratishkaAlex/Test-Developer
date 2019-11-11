from selenium.webdriver.common.by import By

from app.page_object.forms.add_test_form import AddTestForm
from framework.base.base_page import BasePage
from framework.browser.browser import Browser
from framework.elements.button import Button
from framework.elements.label import Label
from framework.elements.link import Link


class ProjectPage(BasePage):
    TABLE_CELL_LOC_PATTERN = "//table[@class='table']//tr//td[{}]"

    def __init__(self):
        super().__init__(By.CSS_SELECTOR, ".panel-heading")
        self._add_test_form = AddTestForm()
        self.__add_test_button = Button(By.CSS_SELECTOR, ".btn-xs", "Add test")
        self.__test_progress_label = Label(By.ID, "pie", "Test progress")

    def get_index_of_column(self, column_name: str) -> int:
        elements_list = Browser().get_elements_list(By.XPATH, "//tr//th")
        for i in range(len(elements_list)):
            if elements_list[i].text == column_name:
                return i + 1
        raise ValueError("There is no such column")

    def get_list_of_column_cells(self, column_name: str) -> list:
        index_of_column = self.get_index_of_column(column_name)
        column_labels_list = Browser().get_elements_list(By.XPATH,
                                                         f"//table[@class='table']//tr//td[{index_of_column}]")
        column_cells_list = list()
        for label in column_labels_list:
            column_cells_list.append(label.text)
        return column_cells_list

    def add_test(self):
        self.__test_progress_label.wait_for_element_visibility()
        self.__add_test_button.wait_and_click()

    def is_test_added(self, test_name) -> bool:
        return self.get_test_link(test_name).is_displayed()

    def get_test_link(self, test_name: str) -> Link:
        return Link(By.XPATH, f"//a[text()='{test_name}']", f"Test {test_name}")

    def navigate_to_test(self, test_name):
        self.get_test_link(test_name).click()

    @property
    def add_test_form(self) -> AddTestForm:
        return self._add_test_form
