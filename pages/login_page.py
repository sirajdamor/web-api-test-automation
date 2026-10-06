from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def error_message(self):
        return self.text_of(self.ERROR)

    def is_login_button_visible(self):
        return self.find(self.LOGIN_BUTTON).is_displayed()
