import pytest
from python.unittesting.to_test import Product


@pytest.fixture
def default_quantity_product():
    return Product('apple', 1)


@pytest.fixture
def product():
    return Product('apple', 1, 100)


def test_default_quantity(default_quantity_product):
    assert default_quantity_product.quantity == 1


def test_setting_quantity(product):
    assert product.quantity == 100


def test_default_subtract_quantity(product):
    product.subtract_quantity()
    assert product.quantity == 99


def test_subtract_quantity_incorrect_args(product):
    with pytest.raises(TypeError):
        product.subtract_quantity('20')


def test_subtract_quantity(product):
    product.subtract_quantity(20)
    assert product.quantity == 80


def test_default_add_quantity(product):
    product.add_quantity()
    assert product.quantity == 101


def test_add_quantity(product):
    product.add_quantity(20)
    assert product.quantity == 120


def test_add_quantity_incorrect_args(product):
    with pytest.raises(TypeError):
        product.add_quantity('20')


def test_change_price(product):
    product.change_price(10)
    assert product.price == 10
