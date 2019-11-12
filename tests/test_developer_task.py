import os
from os.path import abspath, exists

from pytest_testrail.plugin import pytestrail

from app.application_api.api.tests import Tests
from app.application_api.api.token import Token
from app.enums.test_statuses import TestStatuses
from app.models.test import Test
from app.page_object.pages.add_project_page import AddProjectPage
from app.page_object.pages.all_projects_page import AllProjectsPage
from app.page_object.pages.project_page import ProjectPage
from framework.browser.browser import Browser
from framework.models.cookie import Cookie
from framework.test_rail_api.models.user_session import UserSession
from framework.utils.cloudinary_utils import cloudinary_authorize
from framework.utils.logger import Step
from framework.utils.random_utils import get_random_string
from resources import config
from tests.steps.steps import are_tests_sorted_by_date, are_tests_from_page_in_xml, get_test_instance_from_test_page, \
    upload_screenshot_on_cloudinary


class TestDeveloperTask:
    browser = Browser()
    START_TIME_COLUMN_NAME = "Latest test start time"
    TEST_NAME_COLUMN_NAME = "Test name"
    test_rail_user_session = UserSession(config.TEST_RAIL_LOGIN, config.TEST_RAIL_PASSWORD)

    def setup_method(self):
        self.browser.maximize()
        self.browser.set_implicitly_wait(config.TIMEOUT)
        if exists(config.PATH_TO_SAVE_SCREENSHOT):
            os.remove(config.PATH_TO_SAVE_SCREENSHOT)
        if exists(config.PATH_TO_DOWNLOAD_ATTACHMENT):
            os.remove(config.PATH_TO_DOWNLOAD_ATTACHMENT)
        cloudinary_authorize()

    def teardown_method(self):
        self.browser.quit()

    @pytestrail.case("C11345486")
    def test_developer_task(self):
        with Step("Getting token by API request"):
            token = Token().get()

        with Step("Go to site, pass authorization, send cookie with token"):
            self.browser.enter_url(config.URL)
            self.browser.add_cookie(Cookie("token", token))
            self.browser.driver.refresh()
            all_projects_page = AllProjectsPage()
            assert all_projects_page.is_page_opened(), "Variant is not displayed"

        with Step(f"Go to project {config.PROJECT} page, get list of tests"):
            project_id = all_projects_page.projects_menu.get_project_id(config.PROJECT)
            all_projects_page.projects_menu.navigate_to(config.PROJECT)
            project_page = ProjectPage()
            assert project_page.is_page_opened(), f"{config.PROJECT} page wasn't opened"

            start_time_list = project_page.get_list_of_column_cells(self.START_TIME_COLUMN_NAME)
            assert are_tests_sorted_by_date(start_time_list), "Tests on project page are not sorted by date"

            tests_in_xml_string = Tests().get_tests(project_id)
            list_of_tests_names = project_page.get_list_of_column_cells(self.TEST_NAME_COLUMN_NAME)
            assert are_tests_from_page_in_xml(tests_in_xml_string.response_body,
                                              list_of_tests_names), \
                "Not all the tests from first page were gotten from api request"

        with Step("Return to the previous page, click '+Add', enter name of project and save,"
                  " close tab, return to the previous page and refresh page"):
            self.browser.back()
            all_projects_page.projects_menu.add_project()
            add_project_page = AddProjectPage()
            self.browser.switch_to_window(1)
            assert add_project_page.is_page_opened(), "Add project page wasn't opened"

            project_name = f"Project_{get_random_string()}"
            add_project_page.input_project_name(project_name)
            add_project_page.save_project()
            assert add_project_page.is_project_saved(
                project_name), f"There is no message about success saving of project {project_name}"

            self.browser.close_tab()
            self.browser.switch_to_window(0)
            self.browser.refresh_page()
            assert all_projects_page.projects_menu.is_project_displayed(
                project_name), f"Project {project_name} was not added"

        with Step(f"Go to {project_name} page, click on +Add, enter all required fields and attach screenshot,"
                  f" save test and close pop-up"):
            all_projects_page.projects_menu.navigate_to(project_name)
            new_project_page = ProjectPage()
            assert new_project_page.is_page_opened(), f"{project_name} page wasn't opened"

            new_project_page.add_test()
            self.browser.save_screenshot(config.PATH_TO_SAVE_SCREENSHOT)
            new_test = Test(f"test_{get_random_string()}", TestStatuses.FAILED.value, "post", "2016-10-13 09:52:49.0",
                            "2016-10-13 10:01:43.0", "ubuntu",
                            config.BROWSER, abspath(config.PATH_TO_SAVE_SCREENSHOT))
            new_project_page.add_test_form.enter_required_information(new_test)
            new_project_page.add_test_form.submit()
            assert new_project_page.add_test_form.is_test_added_successfully(), "Success notification didn't appear"

            self.browser.click_by_coordinates(0, 0)
            assert new_project_page.is_test_added(new_test.name), "Test wasn't added"

        with Step(f"Go to {new_test.name} page, check that information was entered correctly"):
            new_project_page.navigate_to_test(new_test.name)
            fetched_test = get_test_instance_from_test_page()
            assert new_test == fetched_test, "Information wasn't entered correctly"

        with Step("Upload screenshot on cloudinary and add integration with TestRail"):
            screenshot_public_id = f"screenshot_{get_random_string()}"
            uploaded_screenshot_link = upload_screenshot_on_cloudinary(config.PATH_TO_SAVE_SCREENSHOT,
                                                                       screenshot_public_id)
            self.test_rail_user_session.case.add_result(config.TEST_RAIL_RUN_ID,
                                                        config.TEST_RAIL_CASE_ID,
                                                        uploaded_screenshot_link)
