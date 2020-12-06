from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.utils import ChromeType


def get_chrome():
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    driver.maximize_window()
    return driver


def switch_browser(browser):
    if browser == "chrome":
        return get_chrome()