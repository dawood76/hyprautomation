from selenium.webdriver.common.by import By
from pages.basepage import basePage


class dashboardPage(basePage):
    locator_input = {}
    locator_button = {}
    locator_text = {
        "heading": (By.XPATH, '//div[@class="page-title"]/span')
    }

    def __init__(self,driver):
        super().__init__(driver)

    def validate_dashboard_page_title(self):
        page_title = self.get_text(self.locator_text['heading'])
        assert page_title == 'Dashboard'