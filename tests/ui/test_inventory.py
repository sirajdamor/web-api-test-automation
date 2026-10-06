import pytest

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_six_products_are_shown(inventory):
    assert inventory.item_count() == 6


@pytest.mark.regression
def test_backpack_is_listed(inventory):
    assert "Sauce Labs Backpack" in inventory.item_names()


@pytest.mark.regression
def test_sort_name_a_to_z(inventory):
    inventory.sort_by("za")
    inventory.sort_by("az")
    names = inventory.item_names()
    assert names == sorted(names)


@pytest.mark.regression
def test_sort_name_z_to_a(inventory):
    inventory.sort_by("za")
    names = inventory.item_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.regression
def test_sort_price_low_to_high(inventory):
    inventory.sort_by("lohi")
    prices = inventory.item_prices()
    assert prices == sorted(prices)


@pytest.mark.regression
def test_sort_price_high_to_low(inventory):
    inventory.sort_by("hilo")
    prices = inventory.item_prices()
    assert prices == sorted(prices, reverse=True)
