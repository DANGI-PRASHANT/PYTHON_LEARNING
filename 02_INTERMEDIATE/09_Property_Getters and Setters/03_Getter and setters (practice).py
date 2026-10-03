# 1. Student Marks:

class Student:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def get_marks(self):
        return self.__marks

    @get_marks.setter
    def change_marks(self, new_marks):
        self.__marks = new_marks


s1 = Student(80)

print(s1.get_marks)

s1.change_marks = 90

print(s1.get_marks)


