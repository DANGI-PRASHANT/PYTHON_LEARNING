# Example of writing csv file :


import csv

with open("data.csv","w",newline="") as file:
    writer  = csv.writer(file) # obj creation

    writer.writerow(["Name","Age","Address"])
    writer.writerow(["Angle",7,"Hapure"])
    writer.writerow(["Bipisha",15,"Babarpur"])
    writer.writerow(["Aruna",26,"Hapure"])
    writer.writerow(["Ram",20,"Kathmandu"])
# 
import csv

with open("data_01.csv","w", newline="") as file:
    writer_01 = csv.writer(file)
    writer_01.writerow(["Product","Price","Quantity"])
    writer_01.writerow(["Laptop",120000,2])
    writer_01.writerow(["Mobile",2000,12])
    writer_01.writerow(["Tablets",12000,2])
    writer_01.writerow(["Cell_Phone",20000,5])


# Example of Reading csv file:

import csv

with open("data.csv","r") as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)

# Another example of reading csv file:

import csv 

with open("data_01.csv","r") as file:
    reader_01 = csv.reader(file)

    for line_01 in reader_01:
        print(line_01[0],line_01[2])  #  Accessing specific columns


 # DictReader:  (Dictornary formed)

import csv

with open("data.csv","r") as file:
    reader_02  = csv.DictReader(file)
    for line_02 in reader_02:
        # print(line_02) # Normal print
        print(line_02["name"],line_02["Age"]) # Access specific field



# Writing CSV using DictWriter:

import csv

with open("students.csv", "w", newline="") as file:
    headings = ["name", "age", "city"]

    writer = csv.DictWriter(file, fieldnames=headings)

    writer.writeheader()

    writer.writerow({"name": "Ram", "age": 20, "city": "Kathmandu"})
    writer.writerow({"name": "Shyam", "age": 22, "city": "Lalitpur"})