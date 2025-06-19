import pytest
from src.main import Product, Category


class TestProduct:
    def test_create_product_with_zero_quantity(self):
        with pytest.raises(ValueError) as excinfo:
            Product("Test", "Desc", 100, 0)
        assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)

    def test_create_product_with_negative_quantity(self):
        with pytest.raises(ValueError) as excinfo:
            Product("Test", "Desc", 100, -5)
        assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)

    def test_product_str(self):
        p = Product("Test", "Desc", 100, 5)
        assert str(p) == "Test, 100 руб. Остаток: 5 шт."


class TestCategory:
    def test_average_price_with_products(self):
        p1 = Product("A", "Desc", 100, 2)
        p2 = Product("B", "Desc", 200, 3)
        cat = Category("Test", "Desc", [p1, p2])
        assert cat.get_average_price() == 150.0

    def test_average_price_empty(self):
        cat = Category("Test", "Desc")
        assert cat.get_average_price() == 0.0

    def test_add_product_with_zero_quantity(self):
        cat = Category("Test", "Desc")
        p = Product("Test", "Desc", 100, 1)
        p.quantity = 0
        with pytest.raises(ValueError) as excinfo:
            cat.add_product(p)
        assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


class TestOriginalFunctionality:
    def test_original_tests(self):
        p = Product("Test", "Desc", 100, 5)
        assert p.calculate_total() == 500
        cat = Category("Test", "Desc", [p])
        assert "Test, 100 руб. Остаток: 5 шт." in cat.products
