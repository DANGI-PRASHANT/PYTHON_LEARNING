import json

employee_data = {
    "Name" : "Ram Bahdur kc",
    "Salary" : 120000,
    "Address" : "Pokhara",
    "Employee_id" : "AB34T55 " 
}

with open("data.json","w") as file:
    json.dump(employee_data,file)


# Another example of json:

import json

student_details = {
    "Name": "Anisha Chettri",
    "Age" : 17,
    "Grade" : "Passed High school",
    "Address" : "Tulsipur",
    "Gender": "Female"    
}

with open("data_01.json","w") as file:
    json.dump(student_details,file)


# List also saving inside a json file: (example)

class_10_Friends = ["Ghanshyam","Khagendra","Dibas","Dipesh","Aakash"]

with open("Friends.json","w") as file:
    json.dump(class_10_Friends,file)



# if i have a file but , i have no code in python file . that's time json load sys:


import json

with open("data.json","r") as file:
    data  = json.load(file)

print(data)
print(type(data))


# 1. json.load()

import json

with open("data_01.json","r") as file:
    data_01 = json.load(file)

print(data_01)
print(type(data_01))


# 2. json.load()

import json

with open("Friends.json","r") as file:
    data_02 = json.load(file)

for index, friend in enumerate (data_02,1): # using enumerate
    print(f"{index}. {friend}")
print(type(data_02))


# json.dumps() → Python object → JSON string:

import json 

school = {
    "Name" : "GURUKUL SCHOOL",
    "estd" : 1992,
    "students" : 2000,
    "location" : "Lalitpur",
    "Education_class" : 12

}

json_school = json.dumps(school)

print(json_school)
print(type(json_school))


# Another one:

fruits = ["apple","banana","watermelon",'graphes',"mango"]


json_fruits = json.dumps(fruits)

print(json_fruits)
print(type(json_fruits))


#  json.loads() → JSON string → Python object: 

import json

data_03 = '{"Name": "Ram", "age" : 11,"Location": "Kathmandu"}'

students = json.loads(data_03)
print(students)
print(type(students))

# # Real-world example (API response simulation):

import json 

api_data = '''{
    "Product" : "HP-Laptop",
    "price" : "250000",
    "Rating" : "5 Star",
    "Stock" : 24
} '''

Devices = json.loads(api_data)

print(Devices)
print(type(Devices))

#  Pretty printing JSON:
    # Example 01: 
import json

data_04 = {
    "Name" : "Ram",
    "age" : 25,
    "Location" : "kathmandu"
}

json_string = json.dumps(data_04,indent=4)
print(json_string)

    # Example 02: 

data_05 = {
    "Name"  : "Alex",
    "age" : 23,
    "Location" : "Dang"
}

with open("student.json","w") as file:
    json.dump(data_05,file,indent=4)

