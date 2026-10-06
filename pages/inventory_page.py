from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage


class InventoryPage(BasePage):
    ITEMS = (By.CLASS_NAME, "inventory_item")
    NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT = (By.CLASS_NAME, "product_sort_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def item_count(self):
        self.find(self.ITEMS)
        return len(self.find_all(self.ITEMS))

    def item_names(self):
        self.find(self.NAMES)
        return [e.text for e in self.find_all(self.NAMES)]

    def item_prices(self):
        self.find(self.PRICES)
        return [float(e.text.replace("$", "")) for e in self.find_all(self.PRICES)]

    def sort_by(self, value):
        """value is one of: az, za, lohi, hilo"""
        Select(self.find(self.SORT)).select_by_value(value)

    def add_to_cart(self, product_slug):
        self.click((By.ID, f"add-to-cart-{product_slug}"))

    def remove_from_cart(self, product_slug):
        self.click((By.ID, f"remove-{product_slug}"))

    def cart_count(self):
        badges = self.find_all(self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def wait_for_cart_count(self, expected):
        """Return True if the cart badge shows the expected number within 10 seconds."""
        try:
            WebDriverWait(self.driver, 10).until(lambda d: self.cart_count() == expected)
            return True
        except TimeoutException:
            return False

    def open_cart(self):
        self.click(self.CART_LINK)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
