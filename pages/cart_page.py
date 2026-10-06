from selenium.webdriver.common.by import By

from .base_page import BasePage


class CartPage(BasePage):
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def item_names(self):
        self.wait_for_url_contains("cart")
        return [e.text for e in self.find_all(self.ITEM_NAMES)]

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)
