import pytest
from pages.adminPages.login import loginPage
from pages.adminPages.header import header
from utilities.drivers import switch_browser

@pytest.fixture()
def setup(browser, adminbaseurl):
    global driver, login, headerSection
    driver = switch_browser(browser)
    driver.get(adminbaseurl)
    login = loginPage(driver)
    headerSection = header(driver)
    login.admin_login("admin@hypr.pk", "12345678")
    yield
    driver.close()

def test_admin_can_logout(setup):
    headerSection.logout()
    #validate user has been redirected to the login screen
    login.click_login()

def test_logout_admin_should_not_be_entered_in_app_when_he_she_click_on_back_button_after_logout(setup):
    headerSection.logout()
    driver.execute_script("window.history.go(-1)")
    login.click_login()






