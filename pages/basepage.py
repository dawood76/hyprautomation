from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time


class basePage:

    def __init__(self, driver):
        """

        :rtype: object
        """
        self.browser = driver

    def sendkeys(self, locator, keys):
        time.sleep(0.5)
        elem = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(keys)

    def click_on_elem(self, locator):
        elem = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(locator))
        elem.click()

    def get_text(self, locator):
        elem = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(locator))
        return elem.text

    def get_elem(self, locator):
        elem = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(locator))
        return elem
