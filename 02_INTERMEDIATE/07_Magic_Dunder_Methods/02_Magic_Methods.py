# Real world combined example:

class Product:
    def __init__(self,name ,price):
        self.name = name 
        self.price = price

    def __str__(self):
        return f"Name : {self.name} and Price : {self.price}"

    def __repr__(self):
        return f"Product('{self.name}',{self.price})"

    def __lt__(self,other):
        return self.price < other.price

    def __eq__(self,value):
        return self.price == value
    
p1 = Product("Laptop","200000")
p2 = Product("Mobile","12000")

print(p1)
print(repr(p2))
print(p1 < p2)
print(p1 == p2)
