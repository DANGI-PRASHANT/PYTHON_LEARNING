# 1. __str___(user_Friendly):

class Car:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f" Name: {self.name}"

c1 = Car("maruti")

print(c1)

c2 = Car("Lamborgini")
print(c2)

# Another example :

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name} and Age:{self.age}"

s1 = Student("Ram",55)
print(s1)


# 2. repr (Developer_friendly representation):
        # ---------> Example_01:
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name} and Age: {self.age}"

    def __repr__(self):
        return f"Student('{self.name}',{self.age})"

s1 = Student("Ram",34)
print(s1)
print(repr(s1))


# -------> Example_02:

class Vechicals:
    def __init__(self,name ,color):
        self.name = name 
        self.color = color

    def __str__(self):
        return f"Name: {self.name} and Color: {self.color}"

    def __repr__(self):
        return f"Vechicals('{self.name}','{self.color}')"

v1 = Vechicals("Maruti","Black")
print(v1)
print(repr(v1))


# 3. len(len() Function):

class Team:
    def __init__(self,members):
        self.members = members

    def __len__(self):
        return len(self.members)

t1 = Team(["Ram","shyam","hari"])
print(len(t1))

t2 = Team(["a","b","c","d","e"])
print(len(t2))

t3 = Team("HariBahadur")
print(len(t3))

# Another example:

class Team_1:
    def __init__(self,members,leaders):
        self.members = members
        self.leaders = leaders

    def __len__(self):
        return len(self.members)

t3 = Team_1(["Ram","Hari","baley"],["Krishna","Mohan","Kaley"])
print(len(t3))

t2 = Team_1(["Rita","Gita","Sita"],["Radha","Anisha","Puspa"])
print(len(t3))


# 4. eq (== Operator)

class Car:
    def __init__(self,name):
        self.name = name

    def __eq__(self, value):
        return self.name == value
c1 = Car("Marutii")
c2 = Car("Marutii")

print(c1 == c2)


# 5. lt (less than < operator) with example:

class Student:
    def __init__(self,marks):
        self.marks = marks

    def __lt__(self,other):
        return self.marks < other.marks


s1  = Student(600)
s2 = Student(90)

print(s1 < s2)