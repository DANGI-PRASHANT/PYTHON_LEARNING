
# 1.Create a Student class with __init__() to store name and age.

class Student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def show_details(self):
        print(f"My name is {self.name} and i am {self.age} years old.")

student1 = Student("Ram",12)
student2 = Student('Hari',15)

student1.show_details()
student2.show_details()

# 2.Create a Car class with __init__() to store brand and price.

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_car_details(self):
        print(f"Brand is {self.brand} and Price is {self.price}")


cars = [
    Car("Toyota", 6700000),
    Car("BMW", 8700000),
    Car("Ferrari", 8900000)
]

for car in cars:
    car.show_car_details()


# 3.Create a Book class with __init__() to store title and author.

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def show_book_details(self):
        print(f"Title is {self.title} and Author is {self.author}")

books = [
    Book("Kurushetra","Ram"),
    Book("Muna madhan","laxmi prasad devkota")
]

for book in books:

    book.show_book_details()

# 4. Create a Movie class with __init__() to store movie name and rating.

class Movie:
    def __init__(self,movie_name,rating):
        self.movie_name = movie_name
        self.rating = rating

    def show_movie_detail(self):
        print(f"Movie name is {self.movie_name} and Rating is {self.rating}")


movies = [
    Movie("Avengers","4.5"),
    Movie("Love life" ,"4")
]

for movie in movies:

    movie.show_movie_detail()


# 5. Create a BankAccount class with __init__() to store account holder name and balance.

class Bankaccount:
    def __init__(self,holder_name,balance):
        self.holder_name = holder_name
        self.balance = balance

    def show_bank_details(self):
        print(f"Holder name is {self.holder_name} and Balance is {self.balance}")

banks = [
    Bankaccount("Ram",234500),
    Bankaccount("Shyam",23000)
]

for bank in banks:

    bank.show_bank_details()