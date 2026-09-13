# 2. Super() using with example:

class Nepal:
    def land(self):
        print("We are nepali.")

class People(Nepal):
    def land(self):
        print('i am nepali.')
        super().land() # using here

p1 = People()
p1.land()

# Code Example (constructor case):

class Mother:
    def __init__(self):
        print("I am Mother.")

class Daughter(Mother):
    def __init__(self):
        super().__init__()
        print("I am daughter.")

s1 = Daughter()