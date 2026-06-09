# ✅ What are Classes and Objects?

# 📌 Class
# A class is a blueprint or template used to create objects.
# Just like a blueprint of a house — it defines how the house will look, but it is not an actual house.

# → A class defines attributes (variables) and methods (functions).


# 📌 Object
# An object is the real thing created from the class.
# ✔️ Objects store real data
# ✔️ Each object created from the same class will have its own copy of data


# 📌 Example
# Defining a class named 'Car'
class Car:
    # Constructor to initialize attributes
    def __init__(self, make, model, year):
        self.make = make      # Attribute: make of the car
        self.model = model    # Attribute: model of the car
        self.year = year      # Attribute: year of manufacture

    # Method to display car details
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"  
    
# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

# Accessing object attributes and methods
print(car1.display_info())  # Output: 2020 Toyota Camry
print(car2.display_info())  # Output: 2019 Honda Civic


# In this example:
# - We defined a class named 'Car' with attributes 'make', 'model', and 'year'.
# - We created two objects, 'car1' and 'car2', each with its own data.
# - We accessed the method 'display_info()' to print the details of each car.   
# This demonstrates the concept of classes and objects in Python.
