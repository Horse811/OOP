class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания продукта из словаря."""
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.__products = []
        if products is not None:
            for product in products:
                self.add_product(product)  # Используем наш метод для добавления
        Category.category_count += 1

    def add_product(self, product):
        """Добавляет продукт в категорию с проверкой типа."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        # Проверка на дубликаты по имени
        if product.name in (p.name for p in self.__products):
            raise ValueError(f"Продукт с именем '{product.name}' уже существует в категории")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print("Товары в категории:")
    print(category1.products)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("\nПосле добавления нового товара:")
    print(category1.products)
    print(f"Общее количество товаров: {Category.product_count}")

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера",
         "price": 180000.0, "quantity": 5})

    print("\nИнформация о новом товаре:")
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    print("\nИзменение цены:")
    new_product.price = 800
    print(f"Новая цена: {new_product.price}")

    print("Попытка установить недопустимую цену:")
    new_product.price = -100
    print(f"Цена после попытки изменения: {new_product.price}")
    new_product.price = 0
    print(f"Цена после попытки изменения: {new_product.price}")
