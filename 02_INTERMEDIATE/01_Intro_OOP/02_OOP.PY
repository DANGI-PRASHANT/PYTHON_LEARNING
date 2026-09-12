# CONSTRUCTOR (__init__) - THE HEART OF OBJECT INITIALIZATION:

class Car:
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color

c1 = Car("Maruti",1200000,"black")
c2 = Car("Land cruiser",2000000,"Light black")

print(c1.name)
print(c2.color)
print(c2.price)


#Another example of __Init__:

class student:
    def __init__(self,name,grade,age,location):
        self.name = name
        self.grade = grade
        self.age = age
        self.location = location

s1 = student("Ram",12,17,"Kathmandu")
s2 = student("Shyam",11,15,"Pokhara")
s3 = student("Gita",10,15,"Dang")


print("==============STUDENT DETAILS=================")
print()

print(f"My name is {s1.name}")
print(f"I am currently study in {s1.grade}")
print(f"I am {s1.age} years old.")
print(f"My location is {s1.location}")
print()

print(f"My name is {s2.name}")
print(f"I am currently study in {s2.grade}")
print(f"I am {s2.age} years old.")
print(f"My location is {s2.location}")


