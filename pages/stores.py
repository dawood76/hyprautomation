from selenium.webdriver.common.by import By
from pages.basepage import basePage
from pages.dashboard import dashboardPage


class storesPage(basePage):

    locator_button = {
        "signIn": (By.XPATH, '//button[text()="Sign In"]')
    }
    locator_text = {
        "stores":(By.XPATH, '//h1[text()="Stores"]'),
        "username": (By.XPATH, '(//small[@class="user-text"])[1]')
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard = dashboardPage(driver)

    def click_sign_in(self):
        self.click_on_elem(self.locator_button["signIn"])

    def verify_stores_heading(self):
        heading = self.get_text(self.locator_text["stores"])
        assert heading == "Stores"

    def verify_user_name(self, username):
        un = self.get_text(self.locator_text["username"])
        assert un == username