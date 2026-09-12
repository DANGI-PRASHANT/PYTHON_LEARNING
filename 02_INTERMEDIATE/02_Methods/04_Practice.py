## ALL TOGETHER:

# class Student:
#     school = "ABC School"

#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(self.name, "studies in", self.school)

#     @classmethod
#     def change_school(cls, new_school):
#         cls.school = new_school

#     @staticmethod
#     def info():
#         print("This is a student class")

# s1 = Student("Ram")
# s2 = Student("Shyam")

# s1.show()

# Student.change_school("XYZ School")

# s2.show()

# Student.info()


# Another example:

class School:
    name = "Mount School"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"My name is {self.name} and i am {self.age} years old.")

    @classmethod
    def change_name(cls,new_name):
        cls.name = new_name

    @ staticmethod
    def info():
        print(" i am student.")

s1 = School("Ram",17)
s2 = School("shyam",18)

s1.show_details()
s2.show_details()

School.change_name("Everest Acedamy School")
print(School.name)

School.info()