# __init__() method:
#==================================================================
# ✅ What Is __init__() Method in Python?
# The __init__() method is a special method in Python classes, known as the "constructor".

# It is automatically called when a new object (instance) of the class is created.  
# ➡️ The primary purpose of the __init__() method is to initialize the attributes of the object.
# ➡️ It allows you to set initial values for the object's properties when the object is created.


class Student:
    """
    This class manage students info and activities
    """
    # __init__ method
    def __init__(self, name, age, dept, grade):                   # parameters in __init__ method
        # object_name.attribute_name = value
        self.name = name                             # Student1.name = Alice
        self.age = age                               # Student2.age = 20            
        self.dept = dept                             # Student2.dept = Science            
        self.grade = grade


    # Instance Method
    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Department: {self.dept}, Grade: {self.grade}")

# Creating objects    
Student1 = Student("Alice", 20, "Science", "C") # arguments passed to __init__ method
Student2 = Student("Bob", 22, "Arts", "A")
Student1.display_info()
Student2.display_info()

# This gives all attributes of the class in dictionary
# print(Student1.__dict__)
# print(Student2.__dict__)
"""
When we create an object of the class, python automatically calls the __init__() method and passes the arguments to it.
The first argument is by standard is -> self.
"""

#==================================================================
# Instance variable/attributes are different for different objects
#==================================================================

Student1.grade = "B"        # This will add only for Student1 object, i.e instance var/attr.
Student1.display_info()     # this will print with updated grade "B"
# print(Student1.__dict__)
# print(Student2.__dict__)

Student3 = Student("John", 25, "Commerce", "D")
Student3.display_info()
# print(Student3.__dict__)

# In this example, when we create Student1 and Student2, the __init__() method is called with the provided name and age,
# initializing the respective attributes for each object.   
# The display_info() instance method is then used to print the student's information.
# Note: The __init__() method is optional; if you don't define it, Python provides a default constructor that does nothing.
# However, defining an __init__() method allows you to set up your objects with specific initial values.

