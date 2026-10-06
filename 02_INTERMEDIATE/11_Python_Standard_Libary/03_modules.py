# Random float:

import random

print(random.random() ) # between 0 to 1 numbers are included.


fruits = ["apple","orange","mango","watermelon"]

print(random.choice(fruits))


# Shuffle list:

import random

numbers = [1,2,3,4,5,6,7]  
random.shuffle(numbers) # inside the list items are random position.
print(numbers)

# Random sample:

vechicals = ["car","bike","truck","cycle","bus"]
print(random.sample(vechicals,2))  # if we want to pick up multiple item from the list.

# date & time modules:

from datetime import datetime


print(datetime.now()) # current time

# print(datetime.now().date()) # Only date
# print(datetime.now().time()) # only time

c_time = datetime.now()
print(c_time.date()) # date only
print(c_time.time())  # time only

# Another way:
 
from datetime import date 

print(date.today())

# Custom datetime:

from datetime import date

print(date(2024,2,5))
print(date(2026,2,11))


# Formatting date:

import datetime

now = datetime.datetime.now()

print(now.strftime("%Y-%m-%d"))
print(now.strftime("%H:%M:%S"))


print(now.strftime("%I:%M:%S %p")) # Am and Pm format
print(now.strftime("%I:%M:%S %p"))


# Time difference:

import datetime

t1 = datetime.datetime.now()
t2 = datetime.datetime(2009,2,11)

print(t1-t2)

# Time modules (time control):
 
import time

print("start")
# time.sleep(5)
print("End")

                        # Current time stamp:

import time
print(time.time())

# Example:

start = time.time()

print("Hello world")

end = time.time()

print(end - start)