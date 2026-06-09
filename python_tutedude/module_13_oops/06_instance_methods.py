# ✅ What Are Instance Methods in Python?

# An instance method is a function defined inside a class that works on the object (instance) created from that class.
# ➡️ Instance methods can access and modify object attributes.
# ➡️ They always take -> "self" as the first parameter.

# Example of Instance Methods:

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance Method
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Creating objects
s1 = Student("Amol", 90)
s2 = Student("Riya", 85)

s1.display()
s2.display()

#-------------------------------------------
# 🔍 Explanation
#-------------------------------------------
# display() is an instance method.
# When we call s1.display():
# Python converts it internally to:
# Student.display(s1)
# So self = s1.
#-------------------------------------------

# When we call an instance method using instance/object of the class, python passes the object itself as first argument to that method.
# The first argument is by standard is -> self.


# 🎯 Types of Instance Methods:

# In Python, instance methods are mainly 2 types:

# 1️⃣ Accessor Methods (Getters)
# Used to get/read object data.
# Do NOT modify data.
'''
def get_marks(self):
    return self.marks
'''

# 2️⃣ Mutator Methods (Setters)
# Used to update/modify object data.
'''
def set_marks(self, new_marks):
    self.marks = new_marks
'''

# 📌 Full Example with Getter & Setter

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    # Getter (Accessor)
    def get_balance(self):
        return self.balance
    
    # Setter (Mutator)
    def deposit(self, amount):
        self.balance += amount


acc = BankAccount("Amol", 500)
print(acc.get_balance())
acc.deposit(200)
print(acc.get_balance())



# When to use Instance Methods?

# Use instance methods when:
# -> You want to access attributes of an object.
# -> You want to modify attributes of an object.
# -> You want behavior specific to each object.


# 🧠 Important Points to Remember

# ✔ Instance methods must have self
# ✔ Can access both variables & other methods
# ✔ Different objects → different values
# ✔ Most methods you write in classes are instance methods



# 🟦 Example — Compare static, class, instance methods
class Demo:
    class_var = 10

    def instance_method(self):
        print("Instance method:", self.class_var)

    @classmethod
    def class_method(cls):
        print("Class method:", cls.class_var)

    @staticmethod
    def static_method():
        print("Static method: cannot access class_var directly")

d1 = Demo()
d1.instance_method()        
Demo.instance_method(d1)        # both gives same output
# 🔍 Why Does This Work?
# Instance methods require self
# When you call obj.method(), Python automatically sends obj as self
# When calling through class, Python does NOT send self automatically
# ➝ So we must pass the object manually

d1.class_method()
Demo.class_method()
# 🧠 Why does Python do this?
# Because of the decorator:
# @classmethod

# This decorator modifies the function so that:
# When the method is accessed through the class,
# Python binds the class to the method automatically.

# So Python automatically decides:
# “This method belongs to the class, not an object—
# I should send the class (cls) automatically.”

d1.static_method()
Demo.static_method()
# 🧠 Why does Python do this?
# Because of the decorator:
# @staticmethod
# The purpose of staticmethod:
# A static method is just a helper function placed inside the class for organization.
# It does NOT need:
# -> the object (self)
# -> the class (cls)
# So Python does NOT pass anything.