import pytest
from src.main import Product, Category


@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 599.99, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Техника", [sample_product])


def test_product_init(sample_product):
    assert sample_product.name == "Телефон"
    assert sample_product.description == "Смартфон"
    assert sample_product.price == 599.99
    assert sample_product.quantity == 10


def test_category_init(sample_category, sample_product):
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника"
    assert sample_category.products == [sample_product]


def test_category_count(sample_category):
    assert Category.category_count == 1
    Category("Одежда", "Мода", [])
    assert Category.category_count == 2


def test_product_count(sample_category):
    assert Category.product_count == 1
    p1 = Product("Ноутбук", "Игровой", 1000.0, 5)
    p2 = Product("Наушники", "Беспроводные", 100.0, 20)
    Category("Гаджеты", "Техника", [p1, p2])
    assert Category.product_count == 3
