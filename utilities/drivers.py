from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.utils import ChromeType


def get_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(),chrome_options=chrome_options)


def switch_browser(browser):
    if browser == "chrome":
        return get_chrome()
