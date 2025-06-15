


import pytest
from __main__ import BaseProduct, Product, Smartphone, LawnGrass
from io import StringIO
import sys

def test_abstract_class_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseProduct()

def test_product_implements_abstract_methods():
    p = Product("Test", "Desc", 100, 5)
    assert p.calculate_total() == 500
    assert str(p) == "Test, 100 руб. Остаток: 5 шт."

def test_logging_mixin_output(capsys):
    p = Product("Test", "Desc", 100, 5)
    captured = capsys.readouterr()
    assert "Создан объект Product" in captured.out
    assert "Аргументы: ('Test', 'Desc', 100, 5)" in captured.out

def test_smartphone_inheritance():
    phone = Smartphone("Phone", "Desc", 1000, 2, 3.5, "X", 128, "Black")
    assert isinstance(phone, Product)
    assert isinstance(phone, BaseProduct)
    assert phone.memory == 128

def test_lawn_grass_repr():
    grass = LawnGrass("Grass", "Desc", 500, 10, "Russia", 14, "Green")
    assert repr(grass).startswith("LawnGrass(")
    assert "country='Russia'" in repr(grass)

def test_price_validation():
    p = Product("Test", "Desc", 100, 1)
    with pytest.raises(ValueError):
        p.price = -100