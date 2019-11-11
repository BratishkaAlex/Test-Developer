from os.path import abspath
from xml.etree import ElementTree

from app.models.test import Test
from app.page_object.pages.project_page import ProjectPage
from app.page_object.pages.test_page import TestPage
from framework.utils.cloudinary_utils import cloudinary_upload_file, get_link_to_download_from_cloudinary
from framework.utils.download_utils import decode_base64_to_file
from resources import config

project_page = ProjectPage()
test_page = TestPage()


def are_tests_sorted_by_date(tests_list: list):
    for i in range(len(tests_list) - 1):
        if tests_list[i] < tests_list[i + 1]:
            return False
    return True


def are_tests_from_page_in_xml(xml_string: str, list_of_tests_names: list):
    root = ElementTree.fromstring(xml_string)
    list_names_from_xml = list()
    for test in root:
        list_names_from_xml.append(test.find("name").text)
    return set(list_of_tests_names).issubset(list_names_from_xml)


def get_test_instance_from_test_page() -> Test:
    decode_base64_to_file(test_page.link_to_test_attachment, config.PATH_TO_DOWNLOAD_ATTACHMENT)
    return Test(test_page.test_name, test_page.test_status, test_page.test_method, test_page.time_start,
                test_page.time_end, test_page.test_environment, test_page.test_browser,
                abspath(config.PATH_TO_DOWNLOAD_ATTACHMENT))


def upload_screenshot_on_cloudinary(path_to_image, public_id) -> str:
    cloudinary_upload_file(path_to_image, public_id)
    return get_link_to_download_from_cloudinary(public_id)
