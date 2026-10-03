from mycollection import ram , shyam

print(ram.age)
ram.greet()


print(shyam.age)
ram.greet()


# Direct import :

from mycollection.ram import name , age , greet

print(name)
print(age)
greet()

