# ✅ LEVEL 2 — MULTILEVEL INHERITANCE

# Q6. Three-level hierarchy
# Classes:
# A → B → C
# Each class has its own method.
# Create object of C and call all methods.

# Q7. Constructor Chaining
# A → B → C
# Each has its own constructor.
# Check the order in which constructors execute.

# Q8. Practical Example
# Create:
# Person → Student → CollegeStudent
# Add attributes at each level.
# Print full profile from the bottom-most class.
#==============================================================================================================================================
# Q6. Three-level hierarchy
# Classes:
# A → B → C
# Each class has its own method.
# Create object of C and call all methods.
'''
class A:
    def method_a(self):
        print("This is class A method")

class B(A):
        
    def method_b(self):
        print("This is class B method")

class C(B):

    def method_c(self):
        print("This is class C method")

# Class C inheritates class B and class B inheritates class A, so class C have both class properties.
c = C()
c.method_a()
c.method_b()
c.method_c()
'''

#==============================================================================================================================================
# Q7. Constructor Chaining
# A → B → C
# Each has its own constructor.
# Check the order in which constructors execute.

'''
class A:

    def __init__(self, name):
        print("A constructor called")
        self.name = name

    def method_a(self):
        print("This is class A method, access name")
        print(f"Name: {self.name}")

class B(A):

    def __init__(self, name, age):
        print("B constructor called")
        super().__init__(name)               # Calls A constructor
        self.age = age
    def method_b(self):
        print("This is class B method, access name and age.")
        print(f"Name: {self.name}\nAge: {self.age}")

class C(B):
    def __init__(self, name, age ,blood_group):
        print("C constructor called")
        super().__init__(name, age)         # Calls B constructor (→ A constructor)
        self.blood_group = blood_group
    def method_c(self):
        print("This is class C method, access name, age, blood group.")
        print(f"Name: {self.name}\nAge: {self.age}\nBlood group: {self.blood_group}")

c = C("Alice", 25, "O+") 
# Python executes constructors in the following chain:

# 1️⃣ C constructor
# 2️⃣ B constructor (because super() from C calls B)
# 3️⃣ A constructor (because super() from B calls A)


c.method_a()    # method a will execute
c.method_b()    # method b will execute
c.method_c()    # method c will execute
'''

#==============================================================================================================================================
# Q8. Practical Example
# Create a multilevel inheritance structure with three classes:
# Person
# Attributes: name, age

# Student (inherits from Person)
# Attributes: student_id, grade

# CollegeStudent (inherits from Student)
# Attributes: college_name, course

# Task:
# Initialize all attributes properly using constructors.
# From the CollegeStudent object, print the full profile (all attributes from Person → Student → CollegeStudent).


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        
class Student(Person):

    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

class CollegeStudent(Student):

    def __init__(self, name, age, student_id, grade, college_name, course):
        super().__init__(name, age, student_id, grade)
        self.college_name = college_name
        self.course = course

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.student_id}")
        print(f"Grade: {self.grade}")
        print(f"College Name: {self.college_name}")
        print(f"Course: {self.course}")
        print("================================")


        # ❤️ User-friendly output
    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, "
                f"Grade: {self.grade}, College: {self.college_name}, Course: {self.course}")

    # 🧠 Developer-friendly output (debugging)
    def __repr__(self):
        return (f"CollegeStudent(name={self.name!r}, age={self.age}, "
                f"student_id={self.student_id}, grade={self.grade!r}, "
                f"college_name={self.college_name!r}, course={self.course!r})")


c1 = CollegeStudent("Julie", 22, 101, "A","ABC College", "Computer Science")
c2 = CollegeStudent("Jenny", 22, 101, "A","ABC College", "Computer Science")

c1.display_info()
c2.display_info()

print(c1)        # Calls __str__()
print("========================================================================") 
print(repr(c1))  # Calls __repr__()
print("========================================================================") 

















#==============================================================================================================================================
