class Bank:
    def __init__(self,balance):
        self.__balance = balance

    #Getter: private variables are accesed way is called

    def show_balance(self):
        print(f"Total Balance: ${self.__balance}")

    # Setter : value changing and update directly.

    def change_balance(self,new_balance):
        self.__balance = new_balance



b1 = Bank(1000)

b1.change_balance(2000)
b1.show_balance()


# Another example of getter and setter: (Traditional way)

class Student:
    def __init__(self,name):
        self.__name = name

    # Getter: 

    def show_details(self):
        return self.__name

    # Setter: 

    def change_name(self,new_name):
        self.__name = new_name

s1 = Student("Ram")
s1.change_name("shyam")
print(s1.show_details())

# pythonic way to getter and setter: (Basic Example Getter)

class Teacher:
    def __init__(self,name):
        self.__name = name


    # Getter:
    @property
    def name(self):
        return self.__name

t1 = Teacher("Laxman")
print(t1.name)


# Another example: (Getter)

class Product:
    def __init__(self,name,price):
        self.__name = name
        self.__price = price

    @ property
    def price(self):
        return self.__price
    @property
    def name (self):
        return self.__name

p1 = Product("Alexander",1200)
print(p1.name)
print(p1.price)

# Different type of Example in Rectangle (Getter):

class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width  = width


    @property
    def area(self):
        return self.__length * self.__width

r1 = Rectangle(22,33)
print(f"Area of Rectangle: {r1.area}")
    



