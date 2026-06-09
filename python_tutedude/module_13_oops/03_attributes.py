# Attributes in Python

# Attributes are variables that belong to a class or an object.
# They are used to store data related to the class or object. 
# Attributes help define the properties and characteristics of the class or object.
  
# There are two types of attributes:
# 1. Class Attributes
# 2. Instance Attributes

# 📌 Class Attributes
# Class attributes are shared across all instances of a class.
# They are defined within the class but outside any methods.  
# They can be accessed using the class name or through any instance of the class.

# Example:  
class Dog:
    # Class attribute
    species = "Canis familiaris"  
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)  
dog2 = Dog("Lucy", 5)

# Accessing class attribute
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris

# 📌 Instance Attributes
# Instance attributes are unique to each instance of a class.
# They are defined within the constructor method ( __init__ ) using the self keyword.

# Accessing instance attributes
print(dog1.name)  # Output: Buddy
print(dog1.age)   # Output: 3
print(dog2.name)  # Output: Lucy    
print(dog2.age)   # Output: 5

# In this example:
# - We defined a class named 'Dog' with a class attribute 'species' and instance attributes 'name' and 'age'.
# - We created two instances of the Dog class, 'dog1' and 'dog2', each with its own name and age.
# - We accessed both the class attribute and instance attributes to demonstrate their differences.

# You can also modify instance attributes for each object independently.
dog1.age = 4    
print(dog1.age)  # Output: 4
print(dog2.age)  # Output: 5
# Here, we changed the age of dog1 to 4, while dog2's age remains 5.
# This shows that instance attributes are unique to each object.
