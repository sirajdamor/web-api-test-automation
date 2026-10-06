from selenium.webdriver.common.by import By

from .base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_info(self, first_name, last_name, postal_code):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    def confirmation_text(self):
        return self.text_of(self.COMPLETE_HEADER)

    def error_message(self):
        return self.text_of(self.ERROR)

    def cancel(self):
        self.click(self.CANCEL_BUTTON)
