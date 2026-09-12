# 1. Create a BankAccount class with balance.Add an instance method deposit() to add money and show_balance() to display balance.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"Your balance is ${self.balance}")


account = BankAccount(100)

account.show_balance()

account.deposit(50)

account.show_balance()

# 2. Create a Employee class with name and salary.Add a class variable company = "TechCorp".Use a class method to change company name.

class Employee:
    company = "Techcorp"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"""Name: {self.name}
Salary : {self.salary}""")


    @classmethod
    def change_values(cls,new_name):
        cls.company = new_name

e1 = Employee("Ram",20000)
e1.show_details()
Employee.change_values("Everest Company")
print(f"Company: {Employee.company}")
print()

e2 = Employee("shyam",22000)
e2.show_details()
Employee.change_values("Everest Company")
print(f"Company: {Employee.company}")


# 3. Create a Math class.Add a static method add(a, b) that returns sum of two numbers.

class Math:
    @staticmethod
    def add(a,b):
        print(a + b)

Math.add (5,6)

# 4. Create a Utility class.Add a static method is_even(number) that returns True or False.

class Utility:
    @staticmethod
    def is_even_number(x):
        print("True" if x %2 ==0 else "False")

x = int(input("Enter a number: "))

Utility.is_even_number(x)
