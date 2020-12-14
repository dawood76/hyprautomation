from selenium.webdriver.common.by import By
from pages.basepage import basePage
from pages.dashboard import dashboardPage


class homePage(basePage):

    locator_button = {
        "orderNow": (By.XPATH, '(//button[text()="Order Now"])[1]')
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard = dashboardPage(driver)

    def click_orderNow_button(self):
        self.click_on_elem(self.locator_button["orderNow"])