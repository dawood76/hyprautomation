from selenium.webdriver.common.by import By
from pages.basepage import basePage
from pages.dashboard import dashboardPage

class header(basePage):

    locator_button = {
        "username": (By.XPATH, '//li[@class="nav-item dropdown user-circle"]/a'),
        "logout": (By.XPATH, '//a[contains(text(),"Log Out")]')
    }

    def __init__(self,driver):
        super().__init__(driver)

    def logout(self):
        self.click_on_elem(self.locator_button["username"])
        self.click_on_elem(self.locator_button["logout"])

