import pytest
from pages.homepage import homePage
from pages.stores import storesPage
from pages.signinCustomer import signinCustomer
from pages.header import header
from utilities.drivers import switch_browser
import time

@pytest.fixture()
def setup(browser, baseurl):
    global driver, login, stores, headerSection
    driver = switch_browser(browser)
    driver.get(baseurl)
    home = homePage(driver)
    stores = storesPage(driver)
    login = signinCustomer(driver)
    headerSection = header(driver)
    home.click_orderNow_button()
    headerSection.click_sign_in()
    login.customer_login(1234567891, 12345)
    yield
    driver.close()

def test_user_should_be_logged_out_when_click_on_logged_out_button_from_app_side_bar(setup):
    headerSection.logout()
    stores.verify_stores_heading()

def test_logout_user_should_not_be_entered_in_app_when_he_she_click_on_back_button_after_logout(setup):
    headerSection.logout()
    driver.execute_script("window.history.go(-1)")
    headerSection.click_sign_in()