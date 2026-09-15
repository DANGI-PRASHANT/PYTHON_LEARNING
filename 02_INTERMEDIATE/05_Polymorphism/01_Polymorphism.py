# polymorphism with example:

class Dog:
    def sound(self):
        print("Dog bark.")

class Cat:
    def sound(self):
        print("Cat meows.")

d1 = Dog()
c1 = Cat()

d1.sound()
c1.sound()


# Another example:

class Laptop:
    def feature(self):
        print("it is good for coder.")

class Mobile:
    def feature(self):
        print("It is portable devices.")

l1 = Laptop()
m1 = Mobile()

# d1.study

def gadgate(item):
    item.feature()

gadgate(l1)
gadgate(m1)

# Example:

class House:
    def room(self):
        print("It is big room ")


class Home:
    def room (self):
        print("It is small room ")


h1 = House()
g1 = Home()

def whole_house(rooms):
    rooms.room()

whole_house(h1)
whole_house(g1)


# polymorphism with inheritance (method  overriding style)

# Example_01:

class Animal:
    def sound (self):
        print("This is the sound of animals.")


class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Animal(),Dog(),Cat()]


def produce_sound(object):
    object.sound()

for animal in animals:
    produce_sound(animal)


