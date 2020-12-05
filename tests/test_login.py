import pytest
from pages.login import loginPage
from utilities.drivers import switch_browser
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.utils import ChromeType
import os
import time


class Test_login():

    @pytest.fixture()
    def setup(self, browser):
        self.driver = switch_browser(browser)
        self.driver.maximize_window()
        self.driver.get("https://stageadmin.hypr.pk/")
        self.login = loginPage(self.driver)
        yield
        self.driver.close()

    def test_user_sign_in_with_valid_creds(self, setup):
        self.login.input_email("admin@hypr.pk")
        self.login.input_password("12345678")
        self.login.click_sign_in()
        self.login.validate_user_can_login_with_valid_creds()
        assert True
        time.sleep(10)

    def test_user_sign_in_with_invalid_creds(self, setup):
        self.login.input_email("stageadmin.hypr.pk")
        self.login.input_password("12345678")
        self.login.click_sign_in()






