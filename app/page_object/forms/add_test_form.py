from selenium.webdriver.common.by import By

from app.models.test import Test
from framework.elements.button import Button
from framework.elements.input_field import InputField
from framework.elements.label import Label
from framework.enums.web_element_attributes import WebElementAttributes


class AddTestForm:
    def __init__(self):
        self.__test_name_filed = InputField(By.ID, "testName", "Test name")
        self.__test_method_field = InputField(By.ID, "testMethod", "Test Method")
        self.__test_start_time_field = InputField(By.ID, "startTime", "Start Time")
        self.__test_end_time_field = InputField(By.ID, "endTime", "End Time")
        self.__test_environment_field = InputField(By.ID, "environment", "Environment")
        self.__test_browser_field = InputField(By.ID, "browser", "Browser")
        self.__test_choose_file_field = InputField(By.ID, "attachment", "Attachment")
        self.__save_test_button = Button(By.CSS_SELECTOR, ".form .btn-primary", "Save Test")
        self.__success_message = Label(By.ID, "success", "Success test add notification")

    def get_test_status_option(self, status) -> InputField:
        return InputField(By.XPATH, f"//select[@id='testStatus']//option[text()='{status}']", "Test status")

    def enter_required_information(self, new_test: Test):
        self.__test_name_filed.send_keys(new_test.name)
        self.get_test_status_option(new_test.status).click()
        self.__test_method_field.send_keys(new_test.method)
        self.__test_start_time_field.send_keys(new_test.start_time)
        self.__test_end_time_field.send_keys(new_test.end_time)
        self.__test_environment_field.send_keys(new_test.environment)
        self.__test_browser_field.send_keys(new_test.browser)
        self.__test_choose_file_field.send_keys(new_test.attachment)
        if self.__test_name_filed.get_attribute(WebElementAttributes.VALUE) != new_test.name:
            raise ValueError("Test name wasn't entered in required field")

    def submit(self):
        self.__save_test_button.click()

    def is_test_added_successfully(self) -> bool:
        self.__success_message.wait_for_element_visibility()
        return self.__success_message.is_displayed()
