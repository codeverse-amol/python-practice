# class variables:
#==================================================================
# class variable are defined at the class level.
# same copy of class variables are shared among the instances or objects 
#==================================================================



class Student:
    """
    This class manage students info and activities
    """
    
    # class variables
    college = "ABC College"
    department = ["arts", "commerce", "science"]

    # __init__ method
    def __init__(self, name, age):                   # parameters in __init__ method
        # object_name.attribute_name = value
        self.name = name                             # Student1.name = Alice
        self.age = age                               # Student2.age = 20            
       
    # Instance Method
    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

# Creating objects    
Student1 = Student("Alice", 20) # arguments passed to __init__ method
Student2 = Student("Bob", 22)
Student1.display_info()
Student2.display_info()


# access class variable by objects
print(Student1.college)
print(Student1.department)


# can be accessed by class itself gives same output
print(Student.college)
print(Student.department)

# This gives all instance attributes of the class in dictionary not class attributes.
print(Student1.__dict__)
print(Student2.__dict__)

# help(Student)