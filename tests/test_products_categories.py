import pytest
from src.main import Product, Category


@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 50000, 10)


@pytest.fixture
def sample_category():
    return Category("Электроника", "Техника")


def test_product_creation():
    p = Product.new_product({
        'name': 'Ноутбук',
        'description': 'Игровой',
        'price': 100000,
        'quantity': 5
    })
    assert p.name == 'Ноутбук'
    assert p.price == 100000


def test_price_setter(sample_product):
    sample_product.price = 60000
    assert sample_product.price == 60000
    sample_product.price = -1000  # Должно вывести сообщение об ошибке


def test_category_add_product(sample_category, sample_product):
    initial_count = Category.product_count
    sample_category.add_product(sample_product)
    assert Category.product_count == initial_count + 1
    assert "Телефон, 50000 руб. Остаток: 10 шт." in sample_category.products


def test_private_products_access(sample_category):
    with pytest.raises(AttributeError):
        _ = sample_category.__products
