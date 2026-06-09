# ✅ 3. PRACTICE QUESTIONS — CLASS METHODS (@classmethod)
# Q1. Create a class Mobile with
# class variable brand_name = "Samsung"
# class method change_brand()
# Change brand → check if all objects reflect change.

# Q2. Create a class Student with:
# class variable school_name
# constructor sets name & marks
# class method to change school_name

# Q3. Create class Pizza with:
# class variable base_price = 100
# class method update_base_price()
# Create pizzas before and after update—compare prices.

# Q4. Create factory class method:
# Person.from_string("Rahul-25-Mumbai")
# that returns a Person object from string.

# Q5. Create class Car with:
# class variable total_cars
# increment total every time a car object is created
# (Hint: update inside constructor using class method)

#----------------------------------------------------------------------------------
# Q1. Create a class Mobile with
# class variable brand_name = "Samsung"
# class method change_brand()
# Change brand → check if all objects reflect change.


# Solution:
# class Mobile:
#     brand_name = "Samsung"

#     @classmethod
#     def change_brand(cls, new_brand):
#         cls.brand_name = new_brand
#         print(f"The new brand name is {cls.brand_name}")

# m1 = Mobile()
# m2 = Mobile()
# m3 = Mobile()

# print("Before change:")
# print(m1.brand_name)   # Samsung
# print(m2.brand_name)   # Samsung
# print(m3.brand_name)   # Samsung

# # Calling class method
# Mobile.change_brand("iPhone")

# print("\nAfter change:")
# print(m1.brand_name)   # iPhone
# print(m2.brand_name)   # iPhone
# print(m3.brand_name)   # iPhone

#----------------------------------------------------------------------------------

# Q2. Create a class Student with:
# class variable school_name
# constructor sets name & marks
# class method to change school_name



# Solution:
# class Student:
#     school_name = "ABC School"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @classmethod
#     def change_school(cls, data):
#         cls.school_name = "XYZ School"
#         print(f"The student of {cls.school_name} with name {data.name} has scored {data.marks}")

# s1 = Student("Alice", 85)
# Student.change_school(s1)


# Improved version => 

# class Student:
#     school_name = "ABC School"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @classmethod
#     def change_school(cls, new_name):
#         cls.school_name = new_name

#     def display(self):
#         print(f"{self.name} from {self.school_name} scored {self.marks}")

# s1 = Student("Alice", 85)
# Student.change_school("XYZ School")
# s1.display()

#-----------------------------------------------------------------------------------
# Q3. Create class Pizza with:
# class variable base_price = 100
# class method update_base_price()
# Create pizzas before and after update—compare prices.


# Solution:
# class Pizza:
#     base_price = 100    # class variable

#     @classmethod
#     def update_base_price(cls, new_price):
#         cls.base_price = new_price

#         print(f"Base price updated to: {cls.base_price}")



# p = Pizza()
# # Before update
# print("Before")
# print("Pizze price:", p.base_price)

# # Update using class method
# Pizza.base_price = 200
# # After update
# print("After")
# print("Pizze price:", p.base_price)

# # or

# # Updating class variable using class method
# p.update_base_price(200)
# # or
# Pizza.update_base_price(200)

#-----------------------------------------------------------------------------------

# Q4. Create factory class method:
# Create a class Person with:
# Requirements:
# Instance attributes:
# name
# age
# city
# A factory class method from_string() that takes a string in the format:
# "Rahul-25-Mumbai"
# and returns a Person object.


# Solution:
# class Person:

#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

#     @classmethod
#     def from_string(cls, data):
#         name, age, city = data.split("-")
#         return cls(name, int(age), city)


# p = Person.from_string("Rahul-25-Mumbai")

# print(p.name)
# print(p.age)
# print(p.city)
#-----------------------------------------------------------------------------------
# ✅ Q5 — Redefined Problem Statement

# Create a class Car that keeps track of how many car objects have been created.
# Requirements:
# Create a class variable total_cars initialized to 0.
# Every time a new Car object is created, increase the value of total_cars by 1.
# Use a class method to update the count (Hint: call this method from inside the constructor __init__).
# Create multiple car objects and print the total_cars value to verify that the count increases correctly.


# Solution:
# car class
class Car:
    total_cars = 0
    # constructor
    def __init__(self):
        Car.increment_count()  # calling class method to increment count
    
    @classmethod
    def increment_count(cls):
        cls.total_cars += 1  # incrementing class variable

# creating car objects
c1 = Car()
c2 = Car()
c3 = Car()

# printing total cars created
print("Total car objects created:",Car.total_cars)


