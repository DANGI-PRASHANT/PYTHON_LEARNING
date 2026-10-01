#                       SETTER                                      

class Student:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        self.__name = new_name


s1 = Student("Ram")
s1.name = "shyam"
print(s1.name)                              


        # Another example:

class Teacher:
    def __init__(self,age):
        self.__age = age

    @property               # Getter
    def age(self):
        return self.__age

    @age.setter             # Setter
    def age(self,new_age):
        self.__age = new_age

t1 = Teacher(34)

t1.age = 33
print(t1.age)


# Another example:

class School:
    def __init__(self,students):
        self.__students = students

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self,new_students):
        self.__students = new_students


s1 = School(100)
s1.students = 200
print(s1.students)


# Adding validation: ( Getter and setters)

class Student:
    def __init__(self,age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        if new_age <0:
            print("Age must be positive")
        else:
            self.__age = new_age

s2 = Student(44)
s2.age = -12


print(s2.age)


# Temperature celsius:


class Temperature:
  def __init__(self,celsius):
    self._celsius = celsius
  
  @property
  def celsius(self):
    return self._celsius

  @property
  def fahrenheit(self):
    return (self._celsius * 9/5) + 32
  
  @fahrenheit.setter
  def fahrenheit(self,value):
    self._celsius = (value - 32) * 5/9
  
t1 = Temperature(100)

print(t1.fahrenheit)

t1.fahrenheit = 108
print(t1.celsius)


# Username Rules:

class User:
  def __init__(self,username):
    self.username = username
   
  @property
  def username(self):
    return self._username
  
  @username.setter
  def username(self,value):
    if len(value) < 5:
      print("Must be at least 5 characters.")
    elif " " in value:
      print("No space allowed.")
    else:
      self._username = value


u1 = User('Ram')
print(u1.username)

u1.username = "Shyam"
print(u1.username)

    
