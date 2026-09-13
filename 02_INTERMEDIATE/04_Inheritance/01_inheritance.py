
# Example of inheritance:

class Parent:
    family_nama = "Thapa"
    def property (self):
        print("He is my son")

class Child(Parent):
    pass

c1 = Child()
print(c1.family_nama)
c1.property()


# Another example of inheritance: 
# Single inheritance:

class Headoffice:
    def office(self):
        print("we are good office.")

class Branchoffice(Headoffice):
    def branch(self):
        print("We are best branch .")

b1 = Branchoffice()
b1.branch()
b1.office()


# 2.Multilevel Inheritance:

class Football:
    def skill_1 (self):
        print("It is played by 11 players and our aim is to goal.")

class Clubs(Football):
    def skill_2 (self):
        print("Its aim is to win the club league games.")


class Messi (Clubs):
    def skill_3(self):
        print("He is the best player in world.")

m1 = Messi()
m1.skill_1()
m1.skill_2()
m1.skill_3()


#Another example:

class Motion:
    def chapter_01 (self):
        print ("It is physci books topic")


class Gravity(Motion):
    def chapter_02 (self):
        print("It is law of physic.")

class Viscosity (Gravity):
    def chapter_03(self):
        print("It is also be part of physic")


v1 = Viscosity()
v1.chapter_01()
v1.chapter_02()
v1.chapter_03()



