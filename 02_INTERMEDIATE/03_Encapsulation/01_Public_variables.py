# Public variables with examples:

class Car:
    def __init__(self,name):
        self.name = name

c1 = Car("Maruti")
print(c1.name)

c1.name = "Land cruiser"
print(c1.name)


# Example_01:

class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age

s1 = Student("Ram",12)
print(s1.name)
print(s1.age)

s1.age = 15 # change variables called public variables.
print(s1.age)

