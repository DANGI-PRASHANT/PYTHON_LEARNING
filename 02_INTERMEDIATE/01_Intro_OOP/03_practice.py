#  Methods – Actions Objects Can Perform:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello , my name is {self.name} and i am {self.age} years old")

person1 = Person("alice", 21)
print(person1.name)
print(person1.age)
person1.greet()

# Another example:

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"My name is {self.name} and I am  {self.age} years old.")

student1 = Student("Ram",12)
print(student1.name)
print(student1.age)

student1.greet()


# Another example:

class Hospital:
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
        
    def show_detail (self):
        print(f"My name is  {self.name} , Age is {self.age} and Location is {self.location}")
    

h1 = Hospital("Ram",11,"kathmandu",)
h2 = Hospital("sHyam",16,"Pokhara",)
h3 = Hospital("Hari",15,"Dang")

h1.show_detail()
h2.show_detail()
h3.show_detail()


# Another Example_02:

class Car:
    def __init__(self ,name ,price,color):
        self.name = name
        self.price = price
        self.color = color 

    def show_car_details(self):
        print(f" car name is {self.name}, price is {self.price} and color is {self.price}")

# c1 = Car("Maruti",1300000,"Black")
# c2 = Car("BMW",60000000,"Black")
# c3 = Car("camry"234000,"white")

cars = [Car("Maruti",12300000,"black"),Car("BMW",60000000,"Black"),Car("camry",234000,"white")]

for car in cars:
    car.show_car_details()


# Another example:

class Patients:
    def __init__(self,name ,age,address):
        self.name = name
        self.age = age
        self.address = address

    def show_patients_details(self):
        print(f"My name is {self.name} , I am {self.age} years old and addresss is {self.address}")

patients1 = [Patients("ram",12,"ktm"),Patients("shyam",17,"pkh")]

for patient in patients1:

    patient.show_patients_details()

    