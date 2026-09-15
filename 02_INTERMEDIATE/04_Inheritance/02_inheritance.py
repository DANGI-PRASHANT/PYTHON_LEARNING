# 3. Multiple Inheritance with example:

class Camera:
    def  take_photo(self):
        print("Take photo")

class Phone:
    def call (self):
        print("I am call")

class Smartphone(Camera,Phone):
    def game(self):
        print("I can play game.")

iphone = Smartphone()
iphone.take_photo()
iphone.call()

# another example:

class Sportsclubs:
    def player(self):
        print('Best player in club')


class Business:
    def income(self):
        print("It is also callled business.")

class Football (Sportsclubs,Business):
    def best (self):
        print("Both is important")


f1 = Football()
f1.player()
f1.best()
f1.income()


# Important Concept: Method Resolution Order (MRO)

class Father:
    def skill (self):
        print("I am farmer")

class Mother:
    def skill (self):
        print("I can cook")

class  Son(Mother,Father):  # case of same function name.s
    pass

s1 = Son()
s1.skill()




# Methodd overriding:

class Father:
    def skill (self):
        print("I am farmer.")

class Son(Father):
    def skill (self):
        print("I am doctor")


s1 = Son()
s1.skill

# Another example:

class Vechical:
    def features(self):
        print("It a model or structure.")


class Car(Vechical):
    def features(self):
        print("It is black car")

c1 = Car()
c1.features()
