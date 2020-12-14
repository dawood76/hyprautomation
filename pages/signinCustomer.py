from selenium.webdriver.common.by import By
from pages.basepage import basePage
from pages.dashboard import dashboardPage


class signinCustomer(basePage):

    locator_input = {
        "phoneNumber": (By.XPATH, '//input[@placeholder="Enter Phone Number"]'),
        "password": (By.XPATH, '//input[@placeholder="Enter Password"]')
    }

    locator_button = {
        "signin":(By.XPATH, '//button[text()="Sign in"]')
    }

    location_text = {
        "customerNotFoundSnackBar": (By.XPATH, '//div[text()="CUSTOMER NOT FOUND"]'),
        "wrongPassword": (By.XPATH, '//div[text()="Password is wrong"]')
    }


    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard = dashboardPage(driver)

    def input_phonenumber(self, phoneNumber):
        self.sendkeys(self.locator_input["phoneNumber"], phoneNumber)

    def input_password(self, password):
        self.sendkeys(self.locator_input["password"], password)

    def click_signin(self):
        self.click_on_elem(self.locator_button["signin"])


    def customer_login(self, phonenumber, password):
        self.input_phonenumber(phonenumber)
        self.input_password(password)
        self.click_signin()

    def verify_customer_not_found_snack_bar(self):
        text = self.get_text(self.location_text['customerNotFoundSnackBar'])
        assert text == "CUSTOMER NOT FOUND"

    def verify_wrong_credentials_error(self):
        text = self.get_text(self.location_text['wrongPassword'])
        assert text == "Password is wrong"



