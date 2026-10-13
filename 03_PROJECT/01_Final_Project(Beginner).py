students = []

# Add Student:

def add_student():
    student = {}
    student["id"] = input("Enter your id: ")
    student["name"] = input("Enter your name: ")
    student["age"] = input("Enter your age: ")
    student["grade"] = input("Enter your grade: ")
    students.append(student)
    print("✅ Student added successfully!\n")

# View Students:

def view_students():
    if not students:
        print("No student found.\n")
        return
    
    for student in students:
        print(f"Id:{student["id"]}, name: {student["name"]}, age: {student["age"]},grade: {student["grade"]}")
        print()


 # Function to search student by ID or Name

def search_student():

    query = input("Enter id or name for search: ")
    found = False

    for student in students:
        if  query == student["id"] or query.lower() == student["name"].lower():
            print(f"✅ Found it , Id: {student["id"]}, Name: {student["name"]}, Age: {student["age"]}, Grade: {student["grade"]}")
            found = True

    if  not found:
        print("❌ Student not found.\n")

# Function to update student details

def update_students():
    query = input("Enter student ID to update: ")
    for student in students:
        if student["id"] == query:
            student["name"] = input("Enter your new name: ")
            student["age"] = input("Enter your new age: ")
            student["grade"] = input("Enter your new grade: ")
            print(f"✅ Student details Updated! \n")
            return

        print("❌ Student not found.\n")

# Function to delete student

def delete_student():
    query = input("Enter student ID to delete: ")
    for student in students:

        if student["id"] == query:
            students.remove(student)
            print("✅ Student deleted successfully!\n")
            return

    print("❌ Student not found.\n")


# Function to show total number of students

def total_student():
    print(f"Total Students: {len(students)}\n")


# Main menu
def main_menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View all Students")
        print("3. Search Students")
        print("4. Update Students")
        print("5. Delete Students")
        print("6. Total Students")
        print("7. Exit")
        
        choice = input("Enter a number (1 to 7): ")
        
        if choice == "1":
            add_student()
        
        elif choice == "2":
            view_students()
        
        elif choice == "3":
            search_student()

        elif choice == "4":
            update_students()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            total_student()

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
           print("❌ Invalid choice. Try again.\n")


# Run the program:  

main_menu()

        
        
        

