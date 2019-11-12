import logging
import os

if "LOGIN" in os.environ and "PASSWORD" in os.environ:
    LOGIN = os.environ["LOGIN"]
    PASSWORD = os.environ["PASSWORD"]
else:
    LOGIN = ""
    PASSWORD = ""

if "TEST_RAIL_LOGIN" in os.environ and "TEST_RAIL_PASSWORD" in os.environ:
    TEST_RAIL_LOGIN = os.environ["TEST_RAIL_LOGIN"]
    TEST_RAIL_PASSWORD = os.environ["TEST_RAIL_PASSWORD"]
else:
    TEST_RAIL_LOGIN = ""
    TEST_RAIL_PASSWORD = ""

BROWSER = "chrome"
LANGUAGE = "ru"
PORT = 8080
API_URL = f"http://localhost:{PORT}/api"
URL = f"http://{LOGIN}:{PASSWORD}@localhost:{PORT}/web"
REMOTE_DRIVER_HUB = "qa-auto-nexus"
REMOTE_DRIVER_PORT = 4444
REMOTE_CHROME_VERSION = 72.0
REMOTE_FIREFOX_VERSION = 61.0
TIMEOUT = 10
VARIANT = 2
PROJECT = "Nexage"
TEST_RAIL_URL = "https://tr.a1qa.com"
TEST_RAIL_API_URL = "index.php?api/v2"
TEST_RAIL_RUN_ID = 31131
TEST_RAIL_CASE_ID = 11345486
PATH_TO_SAVE_SCREENSHOT = "resources/screenshot.png"
PATH_TO_DOWNLOAD_ATTACHMENT = "resources/download.png"
LOGGING_LEVEL = logging.INFO
