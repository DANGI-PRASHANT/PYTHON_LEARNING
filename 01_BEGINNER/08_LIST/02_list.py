# 🔶  Adding Items to a List:

fruits = ["apple","banana","orange","Kera","peas"] 

# ✔ append() – Adds item at the END

fruits.append("Mango")
print(fruits)

# ✔ insert(index, value) – Add at a Specific Position:

fruits.insert(1,"Graphes")
print(fruits)

#  ✔ extend(iterable) – Add multiple items:

fruits.extend(["Pear","guava"])
print(fruits)


# 🔶 Changing Existing Items:

    # change one item:

fruits[0] = "cherry"
print(fruits)


    # Change multiple items using slice:

fruits[1:3] = ["Papaya","watermelon"]
print(fruits)

fruits = ["papaya","watermelon","kiwi"] # if no do silicing to added items on the list,
print(fruits)

fruits [1:4] = ["kiwi","ram","shyam","hari","gita","sita"]
print(fruits)



# # 🔶  Removing Items from a List:


# # ✔ remove(value):

colors = ["red","blue","white","Green","Black"]

colors.remove("blue")
print(colors)

# ✔ pop(index):

x = colors.pop(1)
print(f"{x} color is deleted.")


# ✔ del:

del colors[1]
del colors[1:3]
del colors  # to only empty list 

print(colors)


# ✔ clear():

colors.clear() 
print(colors)

# 🔶  Length of List

len(colors)
print(colors)