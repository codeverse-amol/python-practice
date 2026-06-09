# ✅ What is a Class Method?

# A class method is a method that works on the class itself, not on objects.

# ✔️ It has access to class variables
# ✔️ It cannot access object (instance) variables
# ✔️ It uses -> @classmethod decorator
# ✔️ The first parameter is always cls → means "the class itself"

# Syntax:
class MyClass:
    class_var = 10

    @classmethod
    def show(cls):
        print(cls.class_var)

c = MyClass()
c.show()                # can access by object
MyClass.show()          # can access by class itself

# Why do we use cls?
# self -> refers to the object
# cls -> refers to the class

# Just like:
#           Object → self
#           Class → cls

# 👉 Class method used as another way to create object
# 👉 This is called alternative constructor

# 🟦 Class Method vs Static Method vs Instance Method

# | Type                | Uses             | First Parameter | Can access class vars? | Can access object vars? |
# | ------------------- | ---------------- | --------------- | ---------------------- | ----------------------- |
# | **Instance Method** | Normal method    | `self`          |        ✔️              | ✔️                     |
# | **Class Method**    | Work with class  | `cls`           |        ✔️              | ❌                     |
# | **Static Method**   | Utility function | None            |        ❌              | ❌                     |


# 👉 Object can call class method
# 👉 But class method always gets class, never the object


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
d1.class_var = 5
d1.instance_method()  
# output: Instance method: 5
# Because this creates a new variable inside only d1, not in the class.
# So when we call d1.instance_method(), it accesses instance variable first 


d1.class_method() # but class method always gets class, never the object
# output: Class method: 10, this will not consider d1.class_var = 5
# if we do Demo.class_var = 5
Demo.class_var = 5
# then it will print 5
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