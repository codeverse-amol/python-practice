# Duck Typing (Python Special Polymorphism) :
#   -> “If it walks like a duck and quacks like a duck → it's a duck.”
#   -> In Python, Type doesn’t matter — only the presence of methods matters.


#  Example:
class Dog:
    def speak(self):
        print("Bark")

class Human:
    def speak(self):
        print("Hello")

def make_sound(c):
    c.speak()      # No type checking, just calls speak() method  

make_sound(Dog())    # Bark
make_sound(Human())  # Hello 

# ✔ Both objects have speak()
# ✔ So Python allows polymorphism
# ✔ Even though Dog and Human are unrelated classes

# This is duck polymorphism.



# 🎯 Why Duck Typing Is Useful?
# 1. Makes code flexible
# You don't force objects to belong to a specific class.

# file.write()
# network.write()
# logger.write()

# As long as they all implement write(), they work.

# 2. No need for long class hierarchies
# Other languages need this:
# class Animal
#    |
#    → class Dog
#    → class Cat

# Python does not.

# 3. Reduces boilerplate
# No need for interfaces or abstract base classes.

# 🔍 Duck Typing vs Other Polymorphism Types
# Type	                         Based On	                             Example
# Method Overriding	           Inheritance	                    Dog overrides Animal.sound()
# Method Overloading	        Arguments	                        add(2), add(2,3)
# Duck Typing	                Behavior	                    any object with speak() works

# Duck typing is the most powerful and most “Pythonic” form of polymorphism.

# 📝 Duck Typing Example With Built-in Functions
print(len("Amol"))     # 4
print(len([1,2,3]))    # 3
print(len({1,3,5,7}))  # 4
# Different types → len() works

# Because each object implements:
str.__len__

list.__len__

set.__len__

# Python calls the method dynamically → duck polymorphism.


# Summary:
# Polymorphism allows for flexible and reusable code.
# It enables the same interface to be used for different underlying forms (data types).
# Python's dynamic typing and object-oriented features make it easy to implement polymorphism in various ways