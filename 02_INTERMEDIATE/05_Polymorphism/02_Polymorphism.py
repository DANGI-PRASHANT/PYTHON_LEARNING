# Another example:

class Vechical:
    def feature(self):
        print("This is all features of vechicals")

class Car(Vechical):
    def features(self):
        print("it have four wheels.")

class Bus(Vechical):
    def feature(self):
        print("it have many capcity for person. ")


vechicals = [Vechical(),Car(),Bus()]

def overall_feature(item):
    item.feature()

for vechical in vechicals:
    overall_feature(vechical)


# Duck typing (with example): 

class Bird:
   def fly(self):
       print("Bird is flying.")

class Aeroplane:
    def fly(self):
        print("Aeroplane is flying.")

def do_work(item):
    item.fly()

b1 = Bird()
a1 = Aeroplane()

do_work(b1)  # duck typing
do_work(a1) # duck typing