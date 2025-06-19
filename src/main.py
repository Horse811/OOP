
from abc import ABC, abstractmethod
from datetime import datetime


class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        print(f"[{datetime.now()}] Создан объект {self.__class__.__name__}")
        print(f"Аргументы: {args}, {kwargs}")


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def calculate_total(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Product(LoggingMixin, BaseProduct):
    """Основной класс продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        LoggingMixin.__init__(self, name, description, price, quantity)
        BaseProduct.__init__(self, name, description, price, quantity)

    def calculate_total(self) -> float:
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value


class Category:
    """Класс для категорий товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.__products = []
        if products is not None:
            for product in products:
                self.add_product(product)
        Category.category_count += 1

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        if product.quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        if product in self.__products:
            raise ValueError("Товар уже существует в категории")
        self.__products.append(product)
        Category.product_count += 1

    def get_average_price(self) -> float:
        """Возвращает среднюю цену товаров в категории."""
        try:
            return sum(p.price for p in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    @property
    def products(self):
        return "\n".join(str(p) for p in self.__products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == '__main__':
    try:
        broken_product = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            f"Возникла ошибка {type(e).__name__} прерывающая работу программы при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    # Исправленный вызов метода
    print(f"Средняя цена товаров в категории: {category1.get_average_price()} руб.")

    # Пример добавления нового товара
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(f"Обновленная средняя цена: {category1.get_average_price()} руб.")
