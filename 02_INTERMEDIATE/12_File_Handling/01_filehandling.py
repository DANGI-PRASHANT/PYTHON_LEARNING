# syntax: file = open("example.txt","w") ----> open file to write

#file open or create auto and write:

file = open("ram.txt","w")

file.write(f"========================= ABOUT MYSELF=================================\n")
file.write("name = ram prasad dheley\n ")
file.write("Age = 12\n")
file.write("fathername = shyam bahadur dheley\n")
file.write("mothername = patali kumari dheley\n")
file.close()

# Append:

file = open("ram.txt","a")
file.write("Address = Lalitpur\n") 
file.close()

# File Read:

file = open("ram.txt","r")
content = file.read()

print(content)
file.close()

#  Read Line by Line:

file = open("shyam.txt","r")
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
print(line3)
print(line2)
print(line1)

# Doing by loop (automatic):

file = open("shyam.txt","r")
line =file.readline()

while line:
    print(line,end="")
    line = file.readline()
file.close()

# Read All Lines as List:

file = open("shyam.txt","r")  
lines = file.readlines()

result = [line.strip() for line in lines] # strip() ----> remove a species like @,/n,# etc.
print(result)


# using with statement (Recommended) :

with open("shyam.txt","r") as file: # Reading
    content1 = file.read()
    print(content1)

with open("shyam.txt","w") as file: # Writing
    file.write("HEllO WORLD \n") # it is replace another file content.
    file.write("How are you\n")


# Another example of read methods:

# 1. 
with open("shyam.txt","r") as file:
    line = file.readline()

    while line:
        print(line,end="")
        line = file.readline()

# 2. 

with open ("shyam.txt","r") as file:
    lines = file.readlines()

    comp = [line.strip()for line in lines]
    print(comp)

