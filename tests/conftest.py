import os
import re
from datetime import datetime

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

API_BASE_URL = "https://jsonplaceholder.typicode.com"


# ---------------- UI fixtures ----------------
@pytest.fixture
def driver():
    """Start Chrome. Set HEADLESS=1 to run without opening a window (used in CI)."""
    options = Options()
    if os.getenv("HEADLESS", "0") == "1":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def inventory(driver):
    """A browser already logged in as standard_user, on the products page."""
    login = LoginPage(driver).open()
    login.login("standard_user", "secret_sauce")
    page = InventoryPage(driver)
    page.wait_for_url_contains("inventory")
    return page


@pytest.fixture
def checkout_page(driver, inventory):
    """Backpack added to the cart, browser is on checkout step one."""
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.open_cart()
    CartPage(driver).proceed_to_checkout()
    return CheckoutPage(driver)


# ---------------- API fixtures ----------------
@pytest.fixture(scope="session")
def base_url():
    return API_BASE_URL


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"User-Agent": "Mozilla/5.0 (test-automation-framework)"})
    yield s
    s.close()


# ---------------- Screenshot on failure ----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")
        if browser:
            os.makedirs("screenshots", exist_ok=True)
            safe_name = re.sub(r"[^A-Za-z0-9_-]", "_", item.name)
            filename = f"{safe_name}_{datetime.now():%H%M%S}.png"
            browser.save_screenshot(os.path.join("screenshots", filename))
