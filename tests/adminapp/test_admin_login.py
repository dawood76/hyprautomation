import pytest
from pages.adminPages.login import loginPage
from utilities.drivers import switch_browser


@pytest.fixture()
def setup(browser, adminbaseurl):
    global driver, login
    driver = switch_browser(browser)
    driver.get(adminbaseurl)
    login = loginPage(driver)
    yield
    driver.close()


def test_admin_can_login_with_valid_creds(setup):
    login.admin_login("admin@hypr.pk", "12345678")
    login.validate_user_can_login_with_valid_creds()

def test_admin_cannot_login_with_invalid_creds(setup):
    login.admin_login("admin@hypr.pk", "123456789")
    login.verify_wrong_credentials_error()


def test_if_we_try_to_sign_in_with_new_admin_then_it_should_return_an_Alert_of_admin_not_found(setup):
    login.admin_login("adminnew@hypr.pk", "123456789")
    login.verify_user_not_found_error()








