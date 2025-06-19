import pytest
from __main__ import Product, Category


class TestProductInitialization:
    def test_create_product_with_zero_quantity(self):
        with pytest.raises(ValueError) as exc_info:
            Product("Тест", "Описание", 100.0, 0)
        assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"

    def test_create_product_with_negative_quantity(self):
        with pytest.raises(ValueError) as exc_info:
            Product("Тест", "Описание", 100.0, -5)
        assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


class TestCategoryAveragePrice:
    def test_average_price_with_products(self):
        p1 = Product("Товар1", "Описание1", 100.0, 10)
        p2 = Product("Товар2", "Описание2", 200.0, 5)
        category = Category("Категория", "Описание", [p1, p2])
        assert category.get_average_price() == 150.0

    def test_average_price_empty_category(self):
        category = Category("Категория", "Описание")
        assert category.get_average_price() == 0.0

    def test_average_price_single_product(self):
        p = Product("Товар", "Описание", 150.0, 3)
        category = Category("Категория", "Описание", [p])
        assert category.get_average_price() == 150.0


class TestExistingFunctionality:
    def test_product_str_representation(self):
        p = Product("Телефон", "Смартфон", 50000.0, 3)
        assert str(p) == "Телефон, 50000.0 руб. Остаток: 3 шт."

    def test_category_add_product(self):
        p = Product("Ноутбук", "Игровой", 100000.0, 2)
        category = Category("Электроника", "Техника")
        category.add_product(p)
        assert len(category.products.split('\n')) == 1
