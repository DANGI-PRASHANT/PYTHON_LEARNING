# private variables with example(__name ):

class Student:
    def __init__(self,name):
        self.__name = name

s1 = Student("Ram")

print(s1._Student__name)

# Another example:

class Student_1 :
    def __init__(self,location):
        self.__location = location

s2 = Student_1("Kathmandu")

s2.__location = "lalitpur" # this new variables , it is not changed.
print(s2.__location)
print(s2._Student_1__location)


# Example_01:

class Bankaccount:
    def __init__(self,balance):
        self.__balance = balance

    def show_balance(self):
        print(f"Balance is ${self.__balance}")

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance <=amount:
                    print("Insufficent Balance")
        else:
            self.__balance -= amount
        
            
       


ram_account = Bankaccount(5000)
ram_account.deposit(1000)
ram_account.withdraw(100000)

ram_account.show_balance()


# Example_02: Interesting Gaming plater:

class Player:
    def __init__(self,name):
          self.__name = name
          self.__health = 100

    def take_damage(self,damage):
         self.__health -= damage
         if self.__health <0:
              self.__health = 0

    def heal(self,amount):
         self.__health += amount
         if self.__health>100:
              self.__health = 100

    def is_alive(self):
         return self.__health > 0

    def show_health(self):
         print(f"Health is {self.__health}")


p1 = Player("Ram")
p1.take_damage(10)
# p1.heal(15)
p1.show_health()
print(p1.is_alive())

# Example_03 : Youtube video upload sample:

# class Youtube:
#     def __init__(self,name):
#           self.__name = name
#           self.__views = 0
#           self.__likes = 0

#     def show_details(self):
#          print(f"View : {self.__views} , likes: {self.__likes}")

# y1 = Youtube("Python tutorial 1 ")