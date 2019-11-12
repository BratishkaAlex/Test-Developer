import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from resources import config


def get_driver(browser):
    if "isRemote" in os.environ and os.environ["isRemote"] == "true":
        return get_remote_driver(browser)
    return get_local_driver(browser)


def get_local_driver(browser) -> webdriver:
    if browser == "chrome":
        return webdriver.Chrome(ChromeDriverManager().install(),
                                options=get_browser_options(browser))
    elif browser == "firefox":
        return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                 options=get_browser_options(browser))
    else:
        raise ValueError("Unknown browser")


def get_browser_options(browser: str):
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {"intl.accept_languages": str(config.LANGUAGE)}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        return chrome_options
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", str(config.LANGUAGE))
        firefox_options.headless = True
        return firefox_options


def get_remote_driver(browser: str):
    return webdriver.Remote(
        command_executor=f"http://{config.REMOTE_DRIVER_HUB}:{config.REMOTE_DRIVER_PORT}/wd/hub",
        desired_capabilities=get_base_capabilities(browser))


def get_base_capabilities(browser: str):
    capabilities = {
        "browserName": browser
    }
    if browser == "chrome":
        capabilities.update({"version": str(config.REMOTE_CHROME_VERSION)})
    elif browser == "firefox":
        capabilities.update({"version": str(config.REMOTE_FIREFOX_VERSION)})
    else:
        raise ValueError("Unknown browser")
    return capabilities
