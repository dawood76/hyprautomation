from selenium.webdriver.common.by import By
from pages.basepage import basePage
from pages.dashboard import dashboardPage


class header(basePage):

    locator_button = {
        "username": (By.XPATH, '//div[@class="dropdown"]/button'),
        "logout": (By.XPATH, '//button[text()="Logout"]'),
        "signIn": (By.XPATH, '//button[text()="Sign In"]')
    }


    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard = dashboardPage(driver)

    def click_sign_in(self):
        self.click_on_elem(self.locator_button["signIn"])

    def logout(self):
        self.click_on_elem(self.locator_button["username"])
        self.click_on_elem(self.locator_button["logout"])