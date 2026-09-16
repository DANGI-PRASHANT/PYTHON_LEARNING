# simple example:

class Phone:
    def call (self):
        self.connect_network()
        print("Calling...")

    def connect_network(self):
        print("Connect to network....")

p1 = Phone()
p1.call()

# Another example of abstraction:

class Bank:
    def atm(self):
        self.Connect_server()
        print("Connect to Atm")

    def Connect_server(self):
        print("REquest to server....")


b1 = Bank()
b1.atm()

# Abstraction example of bank system: 


class Bankaccount:
    def __init__(self,balance):
        self._balance = balance

    def deposit(self,amount):
        self._balance += amount
    def withdraw(self,amount):
        if self._balance <= amount:
            print("Insufficent balance")
        else:
            self._balance -= amount


    def show_balance(self):
        print(f"Your current balance is {self._balance}")

b1 = Bankaccount(5000)

b1.withdraw(23000)
b1.show_balance()