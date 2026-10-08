# Example 01:

try :
    print(10/0)
except:
    print("You cannot divide by zero")

print("Hello world")
print("Our country is beautiful.")

# Another good practice example:

try :
    print(10/0)
except ZeroDivisionError:
    print("you cannot divided by zero")

except TypeError:
    print(f"You can only divided by interger.")

# Another example:

try : 
    a = int(input("Enter a number: "))
    print(10 / a )

except ZeroDivisionError:
    print("Error: You cannot divide by zero")

except ValueError:
    print("Error: You can only enter a Numberic values.")


# Catch Multiple Exceptions:


try :
    b = int(input("Enter a number: "))
    print(100-b)

except (ZeroDivisionError,ValueError):
    print("Error: Invalid Input")

#  Catch All Exceptions (Not Recommended):

try:
    a = int(input("Enter a number: "))

except Exception as e :
    print(e)


# The "Finally" Block: (compulsary case using finally)
    # simple example:

try: 
    print(10/0)

except ZeroDivisionError:
    print("You cannot divide by zero")

finally:
    print("Hello world")
    print("I like coding.")

# Example (finally) : 

try :
    file = open("Jpt.txt","r")

except FileNotFoundError:
    print("Error: File not Found")

finally:
    print("I like coding.")

    try:
        file.close()

    except:
        pass

# Raising Exceptions:

age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative!")


#  Example: Safe Division Function

def safe_division(a,b):
    try:
        print(a / b)

    except ZeroDivisionError:
        print("Error: cannot by divide by zero")

    except TypeError:
        print("Errro: Can only divide by number.")

    finally:
        print("Division attempt completed")

safe_division(10,2)
safe_division(5,0)
safe_division(4,"a")