# ✅ LEVEL 1 — BASIC INHERITANCE
# Q1. Single Inheritance Basics
# Create two classes:
# Animal → method speak()
# Dog inherits Animal
# Call the parent method from the child.

# Q2. Add Constructor in Parent
# Create class Vehicle with a constructor (brand, model).
# Create Car that inherits Vehicle and prints full details.

# Q3. Override Method
# Create:
# Shape class → method area()
# Circle class → override area()

# Q4. Use super()
# Create:
# Parent Employee with constructor that sets name
# Child Developer adds skills
# Use super() properly.

# Q5. Child Using Parent Variable
# Parent class has:
# company = "TCS"
# Child class prints this variable using inheritance.
#==============================================================================================================================================
# Q1. Single Inheritance Basics
# Create two classes:
# Animal → method speak()
# Dog inherits Animal
# Call the parent method from the child.

'''
class Animal:
    def speak(self):
        print("baw, baw!!")

class Dog(Animal):
    pass

d = Dog()
d.speak()

'''
#==============================================================================================================================================
# Q2. Add Constructor in Parent
# Create class Vehicle with a constructor (brand, model).
# Create Car that inherits Vehicle and prints full details.
'''
class Vehicle:

    def __init__(self,brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):

    def show_details(self):
        print(f"Car Name: {self.brand}\nCar Model: {self.model}")

c = Car("BMW","520d")
c.show_details()
'''
#==============================================================================================================================================
# Q3. Override Method
# Create:
# Shape class → method area()
# Circle class → override area()
'''
class Shape:

    def area(self):
        print("Area not defined for generic shape")

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
        # super().area() --> this will call the parent method explicitly.
    
    # Method overriding
    def area(self):                 # if we comment this method parent method get called.
        print(f"Area of circle: {22/7*self.radius**2}" )      

c = Circle(2)
c.area()

'''
#==============================================================================================================================================
# Q4. Use super()
# Create:
# Parent Employee with constructor that sets name
# Child Developer adds skills
# Use super() properly.
'''
class Employee:

    def __init__(self, name):
        self.name = name 

    def show(self):
        print("Showing the details of employee:")
        print(f"Name: {self.name}")


class Developer(Employee):

    def __init__(self, name, skills):
        super().__init__(name)      # Always call parent FIRST (recommended)
        self.skills = skills        # Child attribute


    def add_skills(self):
        print(f"Skills: {self.skills}")


d = Developer("John", "Python, Django")

d.show()
d.add_skills()

'''
#==============================================================================================================================================
# Q5. Child Using Parent Variable
# Parent class has:
# company = "TCS"
# Child class prints this variable using inheritance.


class Parent:
    company = "TCS"

class Child(Parent):
    pass

c = Child()
print("Company:", c.company)












#==============================================================================================================================================