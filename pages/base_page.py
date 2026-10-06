from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Common helper methods used by every page object."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def text_of(self, locator):
        return self.find(locator).text

    def wait_for_url_contains(self, part):
        return self.wait.until(EC.url_contains(part))
