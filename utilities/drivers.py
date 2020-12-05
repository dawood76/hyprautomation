from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.utils import ChromeType


def get_chrome():
    return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())


def switch_browser(browser):
    if browser == "chrome":
        return get_chrome()