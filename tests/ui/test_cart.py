import pytest

from pages.cart_page import CartPage

pytestmark = pytest.mark.ui

BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"


@pytest.mark.smoke
def test_add_one_item_updates_badge(inventory):
    inventory.add_to_cart(BACKPACK)
    assert inventory.wait_for_cart_count(1)


@pytest.mark.regression
def test_add_two_items_updates_badge(inventory):
    inventory.add_to_cart(BACKPACK)
    inventory.add_to_cart(BIKE_LIGHT)
    assert inventory.wait_for_cart_count(2)


@pytest.mark.regression
def test_remove_item_clears_badge(inventory):
    inventory.add_to_cart(BACKPACK)
    assert inventory.wait_for_cart_count(1)
    inventory.remove_from_cart(BACKPACK)
    assert inventory.wait_for_cart_count(0)


@pytest.mark.regression
def test_cart_page_shows_added_item(driver, inventory):
    inventory.add_to_cart(BACKPACK)
    inventory.open_cart()
    assert CartPage(driver).item_names() == ["Sauce Labs Backpack"]


@pytest.mark.regression
def test_empty_cart_has_no_items(driver, inventory):
    inventory.open_cart()
    assert CartPage(driver).item_names() == []


@pytest.mark.regression
def test_continue_shopping_returns_to_products(driver, inventory):
    inventory.open_cart()
    CartPage(driver).continue_shopping()
    inventory.wait_for_url_contains("inventory")
    assert "inventory" in driver.current_url
