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

# Another example of ABC MOduless:

from abc import ABC, abstractmethod

class website(ABC):
    def show_photo(self):
        print("Photos are shown")

    def show_files(self):
        print("Files are shown")

    @abstractmethod
    def responsive(self):
        pass

class Laptop(website):
    def responsive(self):
        print("Made responsive for laptop")

class Mobile(website):
    def responsive(self):
        print("Made responsive for Mobile.")


l1 = Laptop()
l1.responsive()
l1.show_files()
l1.show_photo()
print()
m1 = Mobile()
m1.responsive()
m1.show_photo()
m1.show_files()


# Another example of abstraction with ABC modulues: (real life)

from abc import ABC,abstractmethod

class Manager(ABC):
    def critical_data(self):
        print(f"Access Cirtical data")


    def modify_rules(self):
        print("I can modify rules.")

    @abstractmethod
    def security(self):
        pass

class Developer(Manager):
    def security(self):
        print("I am developer and i have secured system.")

class Analyst(Manager):
    def security(self):
        print("I am analyst and i have also secured system in my way.")


d1 = Developer()
d1.security()
d1.critical_data()
d1.modify_rules()


a1 = Analyst()
a1.security()
a1.critical_data()
a1.modify_rules()
