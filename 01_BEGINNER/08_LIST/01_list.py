
# How to Create a List: 

fruits = ["apple","banana","Mango","orange"]
print(fruits)


# String convert into list:

word = "HELLO"
word1 = "PYTHON"

print(list(word1))
print(list(word))

# Create Empty List:

empty1 = [] # most used , 
print(empty1)

empty2 = list() # Another way,
print(empty2)


# Characteristics of a List (Very Important Section)


# 1. Mutable (can value change) :

fruits_01 = ["apple","banana","orange"]

fruits_01[1] = "Watermelon" # Here value is changed,
print(fruits_01)


# 2.  Duplicate Values Allowed

Fruits = ["apple","orange","Mango","apple","orange"]
print(Fruits)


# 3.  Can Store Different Data Types Together

mixed = [10, "hello", False, 5.5]

print(mixed)


# 🔶 Accessing Elements (Indexing):

people = ["Ram","shyam","Hari","Gita","Sita"]

print(people[1])
print(people[-1])
print(people[3])



# print(people[8]) # Index error


# 🔶  Slicing (Extracting a Sub-List)

Vechicals = ["cycle","car","Bus","Taxi","Bike","Aeroplane","Helicopter"]

print(Vechicals[1:4])
print(Vechicals[:5])
print(Vechicals[3:5])

print(Vechicals[::-1]) # Reverse Slicing

print(Vechicals[-6:-3]) # Negative silicing
print(Vechicals[-7:]) # Negative silicing 