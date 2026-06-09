# 🔷 What is a Static Method in Python?

# A static method is a method inside a class that does NOT use self (object) and does NOT use cls (class).
# It behaves like a normal function, but it is kept inside the class for organization.
# ✔️ Declared using @staticmethod
# ✔️ Cannot access:
#                   instance variables (self)
#                   class variables (cls)

# ✔️ Can be called using:
#                         Class name → MyClass.method()
#                         Object → obj.method()

# Syntax:
class MyClass:
    @staticmethod
    def show():
        print("I am a static method")


# Usage:
MyClass.show()
obj = MyClass()
obj.show()


# Why use Static Methods?

# Because sometimes you need a function related to a class, but it does not depend on objects or class variables.

# 📌 Example: utility functions
# 📌 Example: validation functions
# 📌 Example: helper functions


# 🟩 Example 1 — Basic Example

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 10))

# Output: 15

# 🔹 No need to create an object
# 🔹 No use of self or cls


# 🟦 Example 2 — Compare static, class, instance methods
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



# 🟨 Real Use Case 1 — Validation Function
class Student:
    def __init__(self, name, age):
        if Student.validate_age(age):
            self.name = name
            self.age = age
        else:
            raise ValueError("Invalid age")

    @staticmethod
    def validate_age(age):
        return 5 <= age <= 25


# ✔️ Static method is used as a helper
# ✔️ No need for self or cls
# ✔️ Keeps code clean inside the class

# 🟧 Real Use Case 2 — Utility Function
import datetime

class Logger:
    @staticmethod
    def current_time():
        return datetime.datetime.now()

# print(Logger.current_time())

# 🟥 When to Use Static Methods? (Interview Answer)

# Use @staticmethod when:
# -> The method does not rely on object (self).
# -> The method does not rely on class (cls).
# -> You want a utility/helper function inside the class for better organization.
# -> You want a method that logically belongs to class but should not modify class or objects.

# 🟩 Common Interview Question
# ❓ Why static method if we already have normal functions?
# 👉 Because it groups utility functions inside the class for better structure.

# Example:
# All string operations inside StringHelper class.



# 🟦 Quick Summary Table
#| Feature	                   Instance Method	                Class Method	                Static Method |      
#|--------------------------   -----------------------------------------------------------------------------  |
#| Uses self	                   ✔️ Yes	                        ❌ No	                        ❌ No   |      
#| Uses cls	                       ❌ No	                           ✔️ Yes	                        ❌ No   |      
#| Access instance variables   	   ✔️ Yes	                        ❌ No	                        ❌ No   |    
#| Access class variables	       ✔️ Yes	                        ✔️ Yes	                         ❌ No   |       
#| Called by object	               ✔️ Yes	                        ✔️ Yes	                         ✔️ Yes  |       
#| Called by class	               ✔️ Yes	                        ✔️ Yes	                         ✔️ Yes  |     