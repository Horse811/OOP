from abc import ABC, abstractmethod
from datetime import datetime


class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        print(f"[{datetime.now()}] Создан объект {self.__class__.__name__}")
        print(f"Аргументы: {args}, {kwargs}")
        # Убираем вызов super().__init__() здесь, так как это миксин


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Изменено с __price на _price для корректной работы наследования
        self.quantity = quantity

    @abstractmethod
    def calculate_total(self) -> float:
        """Рассчитывает общую стоимость товара."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        pass


class Product(LoggingMixin, BaseProduct):
    """Основной класс продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        # Сначала вызываем миксин
        LoggingMixin.__init__(self, name, description, price, quantity)
        # Затем базовый класс
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


# Остальные классы (Smartphone, LawnGrass, Category) остаются без изменений


class Smartphone(Product):
    """Класс для смартфонов."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    """Класс для газонной травы."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)


class Category:
    """Класс для категорий товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        return self.__products

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)
        Category.product_count += 1


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(Category.category_count)  # Исправлено с category1.category_count
    print(Category.product_count)  # Исправлено с category1.product_count

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print([str(p) for p in category2.products])  # Исправлено для лучшего вывода

    print(Category.category_count)
    print(Category.product_count)
