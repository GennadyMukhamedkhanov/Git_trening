class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def create(cls, name, price):
        return cls(name, price)

obj = Product.create('aple', '100')
print(obj.name)
print(obj.price)