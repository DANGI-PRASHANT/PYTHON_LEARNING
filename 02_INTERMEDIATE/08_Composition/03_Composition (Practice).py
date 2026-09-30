# 1. Basic Composition (Engine inside Car)

class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine() 

    def start(self):
        self.engine.start()
        print("car is running")

c1 = Car()
c1.start()


# 2.Computer and CPU:

class CPU :
    def Process(self):
        print("Cpu is starting ")


class Computer:
    def __init__(self):
        self.cpu = CPU()

    def start (self):
        self.cpu.Process()
        print("Computer open")

c2  = Computer()
c2.start()


# 🔹 3. Student and Address

class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country


class Student:
    def __init__(self, city, country):
        self.address = Address(city, country)

    def show_details(self):
        print(f"City: {self.address.city}, Country: {self.address.country}")


s1 = Student("Kathmandu", "Nepal")
s1.show_details()


# 4. Battery inside Mobile

class Battery:
    def charge(self):
        print("Battery is Charging")

class Mobile:
    def __init__(self):
        self.battery = Battery()

    def charge_phone(self):
        self.battery.charge()

m1 = Mobile()
m1.charge_phone()


# 5. Department inside University:

class Department:
    def __init__(self, name):
        self.name = name


class University:
    def __init__(self):
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def show_departments(self):
        for department in self.departments:
            print(department.name)


# Create departments
d1 = Department("Computer Science")
d2 = Department("Business")
d3 = Department("Mathematics")

# Create university
u1 = University()

# Add departments to university
u1.add_department(d1)
u1.add_department(d2)
u1.add_department(d3)

# Print all departments
u1.show_departments()



    


   


