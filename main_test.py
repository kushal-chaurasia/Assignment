import pytest
from main import CheckoutKata, IndividualPrice, SpecialPrice



@pytest.fixture
def pricing_rules():
    return {
        "A": SpecialPrice(special_price_quantity=3, special_price=130, normal_price=50),
        "B": SpecialPrice(special_price_quantity=2, special_price=45, normal_price=30),
        "C": IndividualPrice(price=20),
        "D": IndividualPrice(price=15),
    }


def test_empty_cart(pricing_rules):
    checkout = CheckoutKata(pricing_rules, {})
    assert checkout.calculate_total() == 0


def test_single_item(pricing_rules):
    checkout = CheckoutKata(pricing_rules, {})
    checkout.scan("A")
    assert checkout.calculate_total() == 50


def test_multiple_items(pricing_rules):
    checkout = CheckoutKata(pricing_rules, {})
    checkout.scan("A")
    checkout.scan("B")
    assert checkout.calculate_total() == 80


def test_scan_order(pricing_rules):
    checkout = CheckoutKata(pricing_rules, {})
    checkout.scan("C")
    checkout.scan("D")
    checkout.scan("B")
    checkout.scan("A")
    assert checkout.calculate_total() == 115


def test_discounted_items(pricing_rules):
    checkout = CheckoutKata(pricing_rules, {})
    checkout.scan("A")
    checkout.scan("A")
    assert checkout.calculate_total() == 100

    checkout.scan("A")
    assert checkout.calculate_total() == 130

    checkout.scan("A")
    assert checkout.calculate_total() == 180

    checkout.scan("A")
    assert checkout.calculate_total() == 230

    checkout.scan("A")
    assert checkout.calculate_total() == 260


def test_mixed_items(pricing_rules):
    checkout = CheckoutKata(pricing_rules, {})
    checkout.scan("A")
    checkout.scan("A")
    checkout.scan("A")
    checkout.scan("B")
    assert checkout.calculate_total() == 160

    checkout = CheckoutKata(pricing_rules, {})
    checkout.scan("A")
    checkout.scan("A")
    checkout.scan("A")
    checkout.scan("B")
    checkout.scan("B")
    assert checkout.calculate_total() == 175

    checkout = CheckoutKata(pricing_rules, {})
    checkout.scan("A")
    checkout.scan("A")
    checkout.scan("A")
    checkout.scan("B")
    checkout.scan("B")
    checkout.scan("D")
    assert checkout.calculate_total() == 190

    checkout = CheckoutKata(pricing_rules, {})
    checkout.scan("D")
    checkout.scan("A")
    checkout.scan("B")
    checkout.scan("A")
    checkout.scan("B")
    checkout.scan("A")
    assert checkout.calculate_total() == 190
