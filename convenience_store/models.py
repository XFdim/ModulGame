

from typing import Union

from convenience_store.exceptions import NotProductCart


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return self.name


class ProductCart:
    def __init__(self) -> None:
        self.products = []
        self.amounts = []

    def __str__(self) -> str:
        return ", ".join(map(str, self.products))

    def put(self, product: Product, amount: Union[int, float]) -> None:
        self.products.append(product)
        self.amounts.append(amount)

    def __add__(self, other):
        if not isinstance(other, ProductCart):
            raise NotProductCart(other)
        cart = ProductCart()
        cart.products = self.products + other.products
        cart.amounts = self.amounts + other.amounts

        return cart
