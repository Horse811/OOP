import pytest
from src.main import Product, Category



@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 10000, 5)


@pytest.fixture
def another_product():
    return Product("Ноутбук", "Игровой", 50000, 2)


@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Техника", [sample_product])


class TestProduct:
    def test_str_representation(self, sample_product):
        assert str(sample_product) == "Телефон, 10000 руб. Остаток: 5 шт."

    def test_addition(self, sample_product, another_product):
        assert sample_product + another_product == 10000*5 + 50000*2

    def test_invalid_addition(self, sample_product):
        with pytest.raises(TypeError):
            sample_product + 100

    def test_price_setter(self, sample_product):
        sample_product.price = 15000
        assert sample_product.price == 15000
        sample_product.price = -100
        assert sample_product.price == 15000  # Цена не должна измениться


class TestCategory:
    def test_str_representation(self, sample_category):
        assert str(sample_category) == "Электроника, количество продуктов: 5 шт."

    def test_add_product(self, sample_category, another_product):
        initial_count = Category.product_count
        sample_category.add_product(another_product)
        assert Category.product_count == initial_count + 1
        assert str(another_product) in sample_category.products

    def test_add_invalid_product(self, sample_category):
        with pytest.raises(TypeError):
            sample_category.add_product("Не продукт")

    def test_duplicate_product(self, sample_category, sample_product):
        with pytest.raises(ValueError):
            sample_category.add_product(sample_product)

    def test_total_quantity(self, sample_category, another_product):
        sample_category.add_product(another_product)
        assert str(sample_category) == "Электроника, количество продуктов: 7 шт."
