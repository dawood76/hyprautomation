from selenium.webdriver.common.by import By
from pages.basepage import basePage
from pages.dashboard import dashboardPage


class loginPage(basePage):
    locator_input = {
        "email": (By.XPATH, '//input[@placeholder="Email"]'),
        "password": (By.XPATH, '//input[@placeholder="Password"]')
    }

    locator_button = {
        "signIn": (By.XPATH, '//button[text()="Log in"]')
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard = dashboardPage(driver)


    def input_email(self, email):
        self.sendkeys(self.locator_input['email'], email)

    def input_password(self, password):
        self.sendkeys(self.locator_input['password'], password)

    def click_sign_in(self):
        self.click_on_elem(self.locator_button['signIn'])

    def validate_user_can_login_with_valid_creds(self):
        self.dashboard.validate_dashboard_page_title()

    def user_login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_sign_in()