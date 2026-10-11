# Modif global variables inside function .

num1 = int(input('Enter a number: '))

def change_number():
    global num1
    num1 += 5


change_number()
print(f"Increased by 5 is {num1}")


# Lamdha function:

square = lambda x : x*x
print(square(5))

sub = lambda a,b : a-b
print(sub(45,13))

multiply = lambda a,b : a *b
print(multiply(5,6))


# Function inside functions (simple)

def outer():
    print("It is outer function.")

    def inner():
        print("i am inner function.")
    inner()
outer()


# Docstrings (Function Documentation):

def add(a,b):
    """ 
    This function add two numbers. 
    """
    return a + b
print(add(2,3))
print(add.__doc__)


# Another example:

def product(a,b):
    """
    This is multiplication two numbers.

    """
    return a*b
print(product(9,74))