# Protected variables with example (_name ):


class Product:
    def __init__(self,name):
        self._name = name
    def show_name(self):
        print(f"Product name is {self._name}")

    def change_name (self,new_name):
        self._name = new_name

p1 = Product("Laptop")

p1.change_name("Mobile") # here change name.

p1.show_name()





# Another example_01:

class student:
    def __init__(self,age):
        self._age = age

    def show_age(self):
        print(f"Student age is {self._age}")

    def change_age(self,new_age):
        self._age = new_age


s1 = student(12)

s1.change_age(45)  # here change age.
s1.show_age()


