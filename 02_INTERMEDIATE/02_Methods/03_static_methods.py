# Example_01:

class Person:
    @staticmethod
    def greet():
        print("Good morning")
Person.greet()

# Example_02:

class student:
    @staticmethod
    def greet_01():
        print("Good morning sir . How are you?")
student.greet_01()


# Example_03:

# it is uses as utility function.(mathematics calculation , odd_even etc.)

class Maths1:
    @staticmethod
    def add (a,b):
        print(a+b)

Maths1.add(2,3)

# another: 

class Maths2:
    @staticmethod
    def sub(a,b):
        print(a-b)

    @staticmethod   
    def odd_even(x):
        print("Even" if x %2 ==0 else "odd")


Maths2.sub(5,6)
Maths2.odd_even(23)


