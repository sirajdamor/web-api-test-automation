import pytest

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_complete_checkout(checkout_page):
    checkout_page.fill_info("Siraj", "Damor", "380001")
    checkout_page.finish_order()
    assert "Thank you for your order" in checkout_page.confirmation_text()


@pytest.mark.regression
@pytest.mark.parametrize("first, last, postal, expected", [
    ("", "Damor", "380001", "First Name is required"),
    ("Siraj", "", "380001", "Last Name is required"),
    ("Siraj", "Damor", "", "Postal Code is required"),
])
def test_checkout_missing_information(checkout_page, first, last, postal, expected):
    checkout_page.fill_info(first, last, postal)
    assert expected in checkout_page.error_message()


@pytest.mark.regression
def test_cancel_checkout_returns_to_cart(driver, checkout_page):
    checkout_page.cancel()
    checkout_page.wait_for_url_contains("cart")
    assert "cart" in driver.current_url
