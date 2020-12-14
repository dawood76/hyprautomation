import pytest
from pages.homepage import homePage
from pages.stores import storesPage
from pages.signinCustomer import signinCustomer
from utilities.drivers import switch_browser
import time

@pytest.fixture()
def setup(browser, baseurl):
    global driver, login, stores
    driver = switch_browser(browser)
    driver.get(baseurl)
    home = homePage(driver)
    stores = storesPage(driver)
    login = signinCustomer(driver)
    home.click_orderNow_button()
    stores.click_sign_in()
    yield
    driver.close()

def test_authorized_registered_user_can_login_with_correct_credentials(setup):
    login.customer_login(1234567891, 12345)
    stores.verify_stores_heading()
    stores.verify_user_name("Manal Fatima")

def test_if_we_try_to_sign_in_with_new_number_then_it_should_return_an_Alert_of_CUSTOMER_NOT_FOUND(setup):
    login.customer_login(1233567890, 12345)
    login.verify_customer_not_found_snack_bar()

def test_user_cannot_be_logged_in_with_wrong_creadentials(setup):
    login.customer_login(1234567891, 1234567)
    login.verify_wrong_credentials_error()




