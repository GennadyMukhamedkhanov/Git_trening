class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def create(cls, name, price):
        return cls(name, price)

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_discounted_price(self):
        return self.price - (self.price//100*self.discount)

obj = DiscountedProduct('aple', 100, 5)
print(obj.get_discounted_price())


