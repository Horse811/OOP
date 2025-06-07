import pytest
from __main__ import Product, Smartphone, LawnGrass, Category


@pytest.fixture
def sample_product():
    return Product("Книга", "Художественная", 500, 10)


@pytest.fixture
def smartphone():
    return Smartphone("iPhone", "Смартфон", 100000, 5, 3.5, "15 Pro", 256, "Black")


@pytest.fixture
def lawn_grass():
    return LawnGrass("Трава", "Газонная", 1000, 20, "Россия", 14, "Зеленая")


@pytest.fixture
def sample_category(sample_product):
    return Category("Книги", "Литература", [sample_product])


class TestInheritance:
    def test_smartphone_inheritance(self, smartphone):
        assert isinstance(smartphone, Product)
        assert smartphone.memory == 256
        assert str(smartphone) == "iPhone, 100000 руб. Остаток: 5 шт."

    def test_lawn_grass_inheritance(self, lawn_grass):
        assert isinstance(lawn_grass, Product)
        assert lawn_grass.country == "Россия"
        assert str(lawn_grass) == "Трава, 1000 руб. Остаток: 20 шт."


class TestAddition:
    def test_valid_addition(self, smartphone):
        other = Smartphone("Galaxy", "Смартфон", 80000, 3, 3.2, "S23", 128, "White")
        assert smartphone + other == 100000*5 + 80000*3

    def test_invalid_addition(self, smartphone, lawn_grass):
        with pytest.raises(TypeError):
            smartphone + lawn_grass


class TestCategory:
    def test_add_valid_products(self, sample_category, smartphone, lawn_grass):
        sample_category.add_product(smartphone)
        sample_category.add_product(lawn_grass)
        assert "iPhone" in sample_category.products
        assert "Трава" in sample_category.products

    def test_add_invalid_product(self, sample_category):
        with pytest.raises(TypeError):
            sample_category.add_product("Не продукт")


class TestOriginalFunctionality:
    def test_original_product(self, sample_product):
        assert str(sample_product) == "Книга, 500 руб. Остаток: 10 шт."

    def test_category_str(self, sample_category):
        assert str(sample_category) == "Книги, количество продуктов: 10 шт."
