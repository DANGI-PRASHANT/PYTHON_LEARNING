# 3. Abstraction using ABC module (Advanced but important)


from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print('Dog Barks')

d1 = Dog()
d1.sound()


# Another example:


from abc import ABC , abstractmethod

class Teacher(ABC):
    @abstractmethod
    def skill (self):
        pass

class Student1 (Teacher):
    def skill(self):
        print("Fast learning")

class student2 (Teacher):
    def skill(self):
        print("study")


s1 = Student1()
s1.skill()

s2 = student2()
s2.skill()