from project.drink import Drink
from project.food import Food
from typing import List


class ProductRepository:
    def __init__(self):
        self.products: List[Food, Drink] = []

    def add(self, product: Food or Drink):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join(f"{p.name}: {p.quantity}" for p in self.products)


# food = Food("apple")
# drink = Drink("water")
# repo = ProductRepository()
# repo.add(food)
# repo.add(drink)
# print(repo.products)
# print(repo.find("water"))
# repo.find("apple").decrease(5)
# print(repo)
