import json 

# store student details:

class Student:
    def __init__(self,name):
        self.name = name
        self.courses = []
        self.attendance = {}

    def enroll (self,course_name):
        if course_name not in  self.courses:
            self.courses.append(course_name)
            self.attendance[course_name] = 0

# store Institute details:

class Institute:
    
    def __init__(self,file_name = "data.json"):
        self.filename = file_name
        self.students = {} # Key----> Name, Value---> Student_object
        self.courses = []
        self.load_data()

    def save_data(self):
        data = {
            "students" : {
                name : {
                    "courses" : student.courses,
                    "attendance" : student.attendance
                }

                for name,student in self.students.items()
            },
            "courses": self.courses
        }

        with open("data.json","w") as f:
            json.dump(data,f,indent=4)

    
    def load_data(self):
        try:
            with open("data.json","r") as f:
                data = json.load(f)
                self.courses = data.get("courses",[])
                for name ,info in data.get("students",{}).items():

                    student = Student(name) # composition

                    student.courses = info["courses"]
                    student.attendance = info["attendance"]
                    self.students[name] = student

        except:
            self.courses = []
            self.students = {}

    # Adding courses in institute:

    def add_courses (self,course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"Courses added: {course_name}")

        else:
            print("Courses already exists")

    # Adding student to institute like admission:

    def add_student(self,student_name):
        if student_name not in self.students:
            self.students[student_name] = Student(student_name) # Composition
            print(f"Student added: {student_name}")

        else:
            print("Student already exists")

    # Enrolling student - joining courses:

    def enroll_student(self,student_name,course_name):
        if student_name in self.students and course_name in self.courses:
            self.students[student_name].enroll(course_name)
            print(f"{student_name} enrolled in {course_name}")
        else:
            print("Invalid Student or course")


 # ------------------  ATTENDANCE ------------

    def mark_attendance (self,student_name,course_name):
        if student_name in self.students:
            student = self.students[student_name]

            if course_name in student.attendance:
                student.attendance[course_name] += 1
                print("Attendance Done")

            else:
                print("Student not enrolled")

 # ---------------- ANALYTICS ----------------

    def show_details(self):
        for name ,student in self.students.items():
            print(f"Name: {name}")
            print(f"Courses: {student.courses}")
            print(f"Attendance: {student.attendance}")


    # Most popular courses:

    def most_popular_course(self):
        count = {}

        for student in self.students.values():
            for c in student.courses:
                count[c] = count.get(c,0) + 1  # imp line

        if count:
            popular = max(count,key=count.get)
            print(f"Popular Course: {popular}")
        else:
            print("No Data")

  # ---------------- MENU ----------------

    def menu(self):
        while True:
            print("\n--- Smart Institute System ---")
            print("1. Add Course")
            print("2. Add Student")
            print("3. Enroll Student")
            print("4. Mark Attendance")
            print("5. Show Students")
            print("6. Most Popular Course")
            print("7. Exit Program")

            choice = input("Enter a number(1-7): ")
            if choice == "1":
                self.add_courses(input("Enter Course name: "))
                self.save_data()

            elif choice == "2":
                self.add_student(input("Enter Student name: "))
                self.save_data()

            elif choice == "3":
                self.enroll_student(
                    input("Enter student name: "),
                    input("Enter course name: ")
                )
                self.save_data()

            elif choice == "4":
                self.mark_attendance(
                    input("Enter student name: "),
                    input("Enter course name: ")

                )
                self.save_data()

            elif choice == "5":
                self.show_details()


            elif choice == "6":
                self.most_popular_course()

            elif choice == "7":
                print("Existing Program")
                break
            else:
                print("Invalid Input , Enter 1 to 7")


# ---------------- RUN PROGRAM ----------------

system = Institute()
system.menu() 


