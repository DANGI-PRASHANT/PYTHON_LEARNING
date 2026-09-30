# school ---> student.

class Student:
    def __init__(self,name):
        self.name = name

class School:
    def __init__(self):
        self.name = []

    def add_name (self,name):
        self.name.append(name)

    def show_details(self):
        for name in self.name:
            print(f"Name of student: {name}")

school = School()

school.add_name("Ram")
school.add_name("Hari")
school.add_name("sita")
school.add_name("Gita")

school.show_details()


# ShoppingCart → Product


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Shoppingcart:
    def __init__(self):
        self.product = []

    def add_product(self,name,price):
        product = Product(name,price)
        self.product.append(product)

    def show_details(self):
        for product in self.product:
            print(f"Name: {product.name} , Price: {product.price}")  

shopping = Shoppingcart()

shopping.add_product("Sunescream",190)
shopping.add_product("Mouse",1200)
shopping.add_product("keyboard",4500)

shopping.show_details()


#  Company → Employee

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Company:
    def __init__(self):
        self.Company_name = []

    def add_employees(self,name,salary):
        employee = Employee(name,salary)
        self.Company_name.append(employee)

    def show_details(self):
        for company_name in self.Company_name:
            print(f"Name: {company_name.name}, Salaries : {company_name.salary}")


c1 = Company()
c1.add_employees("Ram",1200)
c1.add_employees("sita",2300)
c1.add_employees("Gita",1280)

c1.show_details()


# Challenging Question : (University → Department → Course)


class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def show_details(self):
        print(f"Department: {self.name}")

        print("Courses:")
        for course in self.courses:
            print(course.name)


class Courses:
    def __init__(self, name):
        self.name = name


class University:
    def __init__(self):
        self.departments = []

    def add_department(self, name):
        department = Department(name)
        self.departments.append(department)
        return department

    def show_details(self):
        for department in self.departments:
            department.show_details()


u1 = University()

# Computer Science Department
d1 = u1.add_department("Computer Science")
d1.add_course(Courses("Python"))
d1.add_course(Courses("Database"))


# Business Department
d2 = u1.add_department("Business")
d2.add_course(Courses("Accounting"))
d2.add_course(Courses("Marketing"))

# Show everything
u1.show_details()





   
        
        


        