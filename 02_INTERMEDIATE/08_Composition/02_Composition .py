# Order system (Real - world):

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.Products = [] # list of object

    def add_product(self,name,price):
        product = Product(name,price) # composition
        self.Products.append(product)

    def show_product(self):
        for product in self.Products:
            print(f"Name: {product.name} , Price: {product.price}")

    def calculation_total(self):
        total = 0
        for product in self.Products:
            total += product.price

        return total

order1 = Order()

order1.add_product("Mobile",120000)
order1.add_product("Laptop",230000)
order1.add_product("Python Book",240)

order1.show_product()
print(f"Total Price: Rs.{order1.calculation_total()}")

