# 2. Class methods (@classmethod):

    # Example:

class Person:
    @classmethod
    def greet(cls):
        print("Good morning")

Person.greet()

# Example_01:

class student:
    @classmethod
    def greet(cls):
        print("Good evening")
student.greet()

# Example_02:

class Organization:
    name = "Ram Organization"

    @classmethod
    def change_name(cls,new_name):
        cls.name = new_name

Organization.change_name("Shyam Organization")
print(Organization.name)

# Example_03:

class School:
    name = "Everest School"

    @classmethod
    def change_name(cls,new_name):
        cls.name = new_name

School.change_name("Mountain School")
print(School.name)

# Example_04: (Important)

class College:
    name = "city colllege"
    estd = 1983
    student = 5000

    @classmethod
    def change_values(cls,new_name,new_estd,new_student):
        cls.name = new_name
        cls.estd = new_estd
        cls.student = new_student

College.change_values("Global college",1990,2500)
print(College.name)
print(College.estd)
print(College.student)