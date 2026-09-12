class Car:
    # attributes / properties:
    wheels = 4
    steering = 1
    engine = "strong"
    color = "blue"
    top_speed = 124

car1 = Car() # object creation:
print(car1.wheels)
print(car1.steering)
print(car1.engine)
print(car1.top_speed)


class House:
    # attributes/properties:
    doors = 30
    windows = 20
    rooms = 8
    bathroom = 12
    area = "1 ropani"

house1 = House() # object creation:
print(house1.doors)
print(house1.windows)
print(house1.rooms)
print(house1.bathroom)
print(house1.area)


        # Methods:

class Car:
    def speed(self):
        print("I am very fast.")

car1 = Car()
car1.speed()

# Example_01:


class Book:
    def copy(self):
        print("It is very interested book.")

book1 = Book()
book1.copy()

# Example_02: 


class House:
    def quality(self):
        print("It is very strong house .")

house1 = House()
house1.quality()

# Example_03:

class Laptop:
    def quality_01(self):
        print("Best for gaming")

laptop1 = Laptop()
laptop1.quality_01

# Example_04:

class Student:
    # attributes / properties:

    name = "shyam"
    grade = 12

    # methods:

    def username(self):
        print("Username is shyam123")

    def location(self):
        print("Location is kathmandu")

s1 = Student()
print(s1.name)
print(s1.grade)
print()

s1.username()
s1.location()


# Example_05:

class Hospital:
    # attriutes/properties:
    name = "shyam"
    age = 12


    def location(self):
        print(f"Mu location is Kathmandu.")

    def height(self):
        print(f"My height is 5.6")

h1 = Hospital()
print(h1.name)
print(h1.age)

h1.location()
h1.height()
