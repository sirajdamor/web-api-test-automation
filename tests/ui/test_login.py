import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_valid_login(driver):
    login = LoginPage(driver).open()
    login.login("standard_user", "secret_sauce")
    login.wait_for_url_contains("inventory")
    assert "inventory" in driver.current_url


@pytest.mark.regression
@pytest.mark.parametrize("username, password, expected", [
    ("locked_out_user", "secret_sauce", "locked out"),
    ("standard_user", "wrong_password", "do not match"),
    ("", "", "Username is required"),
])
def test_invalid_login(driver, username, password, expected):
    login = LoginPage(driver).open()
    login.login(username, password)
    assert expected in login.error_message()


@pytest.mark.regression
def test_password_required(driver):
    login = LoginPage(driver).open()
    login.login("standard_user", "")
    assert "Password is required" in login.error_message()


@pytest.mark.regression
def test_logout(driver, inventory):
    inventory.logout()
    assert LoginPage(driver).is_login_button_visible()


@pytest.mark.regression
def test_cannot_open_inventory_without_login(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    assert "logged in" in LoginPage(driver).error_message()
