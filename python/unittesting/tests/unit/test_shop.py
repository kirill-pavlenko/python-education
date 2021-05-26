import pytest
from python.unittesting.to_test import Product, Shop


product = Product('apple', 20, 300)
products_list = [Product('orange', 10, 300), Product('banana', 20, 100)]


@pytest.fixture
def default_shop():
    return Shop()


@pytest.fixture
def one_products_shop():
    return Shop(product)


@pytest.fixture
def many_products_shop():
    return Shop(products_list)


def test_default_shop(default_shop):
    assert default_shop.products == []


def test_one_products_shop(one_products_shop):
    assert one_products_shop.products == [product]


def test_many_products_shop(many_products_shop):
    assert many_products_shop.products == products_list


def test_get_product_index(many_products_shop):
    assert many_products_shop._get_product_index('orange') == 0


def test_get_product_index_nonexistent_product(many_products_shop):
    assert many_products_shop._get_product_index('apple') is None


def test_add_product(default_shop):
    default_shop.add_product(product)
    assert default_shop.products == [product]


def test_default_sell_product(many_products_shop):
    assert many_products_shop.sell_product('banana') == 20.0


def test_sell_product(many_products_shop):
    assert many_products_shop.sell_product('banana', 11) == 220.0


def test_sell_product_value_error(one_products_shop):
    with pytest.raises(ValueError):
        one_products_shop.sell_product('apple', float('inf'))


def test_sell_product_products_left(one_products_shop):
    one_products_shop.sell_product('apple', 100)
    assert one_products_shop.products[0].quantity == 200


def test_sell_product_no_products_left(one_products_shop):
    one_products_shop.sell_product('apple', product.quantity)
    assert product not in one_products_shop.products
