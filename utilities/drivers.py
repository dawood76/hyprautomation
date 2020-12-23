from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options


def get_chrome():
    chrome_options = Options()
    #chrome_options.add_argument("--window-size=1920,1080");
    chrome_options.add_argument("--start-maximized");
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), chrome_options=chrome_options)
    driver.maximize_window()
    return driver


def switch_browser(browser):
    if browser == "chrome":
        return get_chrome()