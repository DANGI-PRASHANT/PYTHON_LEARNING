# Example of Composition :

class Engine:
    def start(self):
        print("four cylinder engine.")

class Musicsystem:
    def play(self):
        print("Playing Music...")

class Car:
    def __init__(self):
        self.engine = Engine()
        self.music = Musicsystem()

    def show_details(self):
        self.engine.start()
        self.music.play()
        print("Now, Car is Ready for Ride.")

    

c1 = Car()
c1.show_details()


# Another example of composition: (School based)

class Student:
    def skill (self):
        print(f'I have multi-tasking ability')

class Teacher:
    def skill_1 (self):
        print("I have best teaching skill.")


class School:
    def __init__(self):
        self.student = Student()
        self.Teacher = Teacher()

    def show(self):
        self.student.skill()
        self.Teacher.skill_1()
        print(f"we have best teacher and student in our school.")

s1  = School()
s1.show()


# Another example of Composition : (Mobile based)

class Call :
    def phone_call(self):
        print(f"Calling a person...")

class Camera:
    def photo(self):
        print(f"I can caputre a photo")

class Music:
    def play(self):
        print(f"I can play a music")

class Mobile:
    def __init__(self):
        self.call = Call()  # here is a compositon doing.
        self.camera = Camera()
        self.Music = Music()

    def show_details_1(self):
        self.call.phone_call()
        self.camera.photo()
        self.Music.play()
        print("This is a simple system of mobile demo")

m1 = Mobile()
m1.show_details_1()


# Another example of composition ( Game character design-Real world example): 

class Health:
    def __init__(self,hp):
        self.hp = hp

    def heal (self,amount):
        self.hp += amount

    def take_damage(self,amount):
        self.heal -= amount

class Inventory:
    def __init__(self):
        self.items = []

    def add_item (self,item):
        self.items.append(item)

    def show_item(self):
        print(f"Inventory: {self.items}")

class Player:
    def __init__(self):
        self.Health = Health(100)
        self.Inventory = Inventory()

    def status(self):
        print(f"HP: {self.Health.hp}")


p1 = Player()

p1.Inventory.add_item("Knife")
p1.Inventory.add_item("Helmet")
p1.Inventory.add_item("armour")

p1.Health.heal(20)
p1.Health.take_damage(55)
p1.status()

p1.Inventory.show_item()