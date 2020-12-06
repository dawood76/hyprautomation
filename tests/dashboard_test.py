import pytest
from pages.login import loginPage
from pages.dashboard import dashboardPage

from utilities.drivers import switch_browser
import time


@pytest.fixture()
def before_each(browser, baseurl):
    global driver, dashboard
    driver = switch_browser(browser)
    driver.get(baseurl)
    login = loginPage(driver)
    login.user_login("admin@hypr.pk", "12345678")
    dashboard = dashboardPage(driver)
    yield
    driver.close()


def test_dashboard(before_each):
    dashboard.validate_dashboard_page_title()


def test_dashboard_title(before_each):
    dashboard.validate_dashboard_page_title()
