import logging
import os

if "LOGIN" in os.environ and "PASSWORD" in os.environ:
    LOGIN = os.environ["LOGIN"]
    PASSWORD = os.environ["PASSWORD"]
else:
    LOGIN = ""
    PASSWORD = ""

BROWSER = "firefox"
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
PATH_TO_SAVE_SCREENSHOT = "resources/screenshot.png"
PATH_TO_DOWNLOAD_ATTACHMENT = "resources/download.png"
LOGGING_LEVEL = logging.INFO
