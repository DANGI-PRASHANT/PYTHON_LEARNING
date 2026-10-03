import Math_modulus

print(Math_modulus.weight)
Math_modulus.greet()
Math_modulus.Hello()


# ..... import

import math 

print(math.sqrt(25))
print(math.pi)

# from ...import 

from math import sqrt , pi

print(sqrt (6))
print(pi)


from math import sqrt , pi

print(sqrt(49))
print(pi)


# i want to from own modules:

from Math_modulus import age , greet, Hello ,motey


print(age)
greet()
Hello()

import Math_modulus as mm

print(mm.weight)


# name == "main" pattern: 

import Math_modulus as mm

