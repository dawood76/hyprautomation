from selenium.webdriver.common.by import By
from pages.basepage import basePage
from pages.dashboard import dashboardPage


class loginPage(basePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard = dashboardPage(driver)

    locator_input = {
        "email": (By.XPATH, '//input[@placeholder="Email"]'),
        "password": (By.XPATH, '//input[@placeholder="Password"]')
    }
    locator_button = {
        "login": (By.XPATH, '//button[text()="Log in"]')}

    location_text = {
        "wrongPassword": (By.XPATH, '//span[text()="Password is wrong"]'),
        "adminNotFound": (By.XPATH, '//span[text()="adminnew@hypr.pk is not found"]')
    }

    def input_email(self, email):
        self.sendkeys(self.locator_input["email"], email)

    def input_password(self, password):
        self.sendkeys(self.locator_input["password"], password)

    def click_login(self):
        self.click_on_elem(self.locator_button["login"])

    def validate_user_can_login_with_valid_creds(self):
        self.dashboard.validate_dashboard_page_title()

    def verify_wrong_credentials_error(self):
        text = self.get_text(self.location_text['wrongPassword'])
        assert text == "Password is wrong"

    def verify_user_not_found_error(self):
        text = self.get_text(self.location_text["adminNotFound"])
        assert text == "adminnew@hypr.pk is not found"

    def admin_login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login()


