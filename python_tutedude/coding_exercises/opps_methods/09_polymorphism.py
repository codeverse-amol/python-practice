# 🔥 BEGINNER-LEVEL POLYMORPHISM QUESTIONS
# Q1. Duck Typing
# Create two classes:
# Cat with method sound() → prints "Meow"
# Dog with method sound() → prints "Bark"
# Write a function make_sound(animal) that works for both.

# Q2. Same method name, different output
# Create classes Car, Bike → both implement wheels() method but return different numbers.

# Q3. Polymorphic function
# Write a function area() that accepts any object having method calculate_area() (Circle, Square, etc.).

# Q4. Polymorphism with loops
# Store objects of different classes in a list and call the same method on each.
#---------------------------------------------------------------------------------------------

# ⭐ INTERMEDIATE-LEVEL QUESTIONS
# 5️⃣ Method Overriding
# Create:
# Class Employee → method work()
# Class Developer(Employee) → override work()
# Class Tester(Employee) → override work()
# Call work() polymorphically.

# 6️⃣ super() + overriding
# Parent class Animal → method sound().
# Child class Dog:
# Override sound()
# Call super().sound() also.

# 7️⃣ Multiple inheritance + MRO
# Create classes:
# A → method show()
# B → method show()
# C(A, B) → call show()
# Observe which method runs (MRO).

# 8️⃣ Abstract Class Polymorphism
# Create abstract class Shape:
# abstract method area()
# Create subclasses:
# Rectangle
# Triangle
# Use polymorphism to print areas of both.

#---------------------------------------------------------------------------
# 🔥 ADVANCED-LEVEL QUESTIONS (for mastery)
# 9️⃣ Operator Overloading
# Create a Point class (x, y).
# Overload:
# + → add two points
# == → check if coordinates are equal

# 🔟 Overload __str__ + __repr__
# Build a class Book:
# Overload __str__ → user-friendly
# Overload __repr__ → developer-friendly
# Print object in list context & directly to observe difference.

# 1️⃣1️⃣ Runtime Polymorphism With Composition
# Create:
# Class NotificationSender
# Subclasses: EmailSender, SMSSender
# Another class NotificationService that accepts any sender object and calls send().

# 1️⃣2️⃣ Polymorphism inside inheritance chain
# Create:
# Class Person → method role()
# Subclass Student → role()
# Subclass Teacher → role()
# Use a loop to call role() on mixed objects.

# 1️⃣3️⃣ Polymorphism with exception handling
# Create objects of different classes that may raise different errors in a common method call.
# Use polymorphism to handle them generically.

# 1️⃣4️⃣ Method Overloading (Python way)
# Create a class Calculator with a single method add() that accepts:
# 2 arguments → add
# 3 arguments → add
# 1 argument → return same
# (Use *args or default parameters.)
#------------------------------------------------------------------------------------------------

# Q1. Duck Typing
# Create two classes:
# Cat with method sound() → prints "Meow"
# Dog with method sound() → prints "Bark"
# Write a function make_sound(animal) that works for both.
'''
class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()


make_sound(Dog())
make_sound(Cat())
'''
#------------------------------------------------------------------------------------------------
# Q2. Same method name, different output
# Create classes Car, Bike → both implement wheels() method but return different numbers.
'''
class Car:

    def wheels(self):
        return 4
class Bike:

    def wheels(self):
        return 2
    
vehicles = [Car(), Bike()]

for v in vehicles:
    print(f"No of wheels: {v.wheels()}")
'''

#------------------------------------------------------------------------------------------------

# Q3. Polymorphic function
# Write a function area() that accepts any object having method calculate_area() (Circle, Square, etc.).
'''
import math
class Circle:

    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return math.pi * self.r**2
    
class Square:
    def __init__(self, a):
        self.a = a
    def calculate_area(self):
        return self.a**2
    

def area(obj):
    return obj.calculate_area()

print(area(Circle(5)))
print(area(Square(4)))
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Q4. Polymorphism with loops
# Create three different classes, for example Dog, Cat, and Cow.
# Each class should have a method with the same name, such as sound(), but each class should return a different output representing the sound that animal makes.

# After creating the classes:
# 1. Create one object of each class.
# 2. Store all these objects inside a single list (like animals = [Dog(), Cat(), Cow()]).
# 3. Use a for loop to iterate through the list.
# 4. Inside the loop, call the same method (sound()) on every object, without checking the type of the object.

# This will demonstrate polymorphism, because:
# -> The loop calls the same method name,
# -> But each object executes its own class’s version of that method,
# -> Producing different outputs.

# Goal: Show how Python automatically selects the correct method for each object at runtime when used inside a loop.

# class Dog:
#     def sound(self):
#         return "Bark"
# class Cat:
#     def sound(self):
#         return "Meow"
# class Cow:
#     def sound(self):
#         return "mhaaaa"

# animals = [Dog(), Cat(), Cow()]

# for a in animals:
#     print(a.sound())


# => Advanced Polymorphism Example: Different Payment Methods
# Imagine you are building an app that accepts multiple payment methods:

# 1.Credit Card
# 2.UPI
# 3.PayPal

# Each payment method has a method called pay(amount), but the logic inside is different.
'''
class Credit_Card:

    def pay(self,amount):
        return f"₹{amount} paid by Credit Card."
class UPI:

    def pay(self,amount):
        return f"₹{amount} paid by UPI."
class PayPal:

    def pay(self,amount):
        return f"₹{amount} paid by PayPal."
    
# List of different payment methods
payments = [Credit_Card(), UPI(), PayPal()]

# Polymorphic behavior
for payment in payments:
    print(payment.pay(500))
'''


# What makes this an advanced example?
# 1. Same method name → pay()
# -> But each class processes payment differently.

# 2. More realistic:
# -> Real systems (Amazon, Swiggy, Ola, etc.) use the same idea — they don’t write separate code for each payment type. They use polymorphism.

# 3. Better scalability:
# -> If you add a new payment method tomorrow:

# class Crypto:
#     def pay(self, amount):
#         return f"Paid ₹{amount} using Bitcoin"

# -> You do not change any other code.
# -> Just add it to the list:
#       '''payment_methods.append(Crypto())'''
# -> The loop will automatically work.

# 4. This is the basis of Strategy Pattern
# -> A major design pattern in OOP relies on this exact polymorphism concept.

#--------------------------------------------------------------------------------------------

# ⭐ INTERMEDIATE-LEVEL QUESTIONS
# Q.5 Method Overriding
# Create the following classes:

# Employee
# Create a method work() that prints:
#   -> "Employee is working"

# Developer (inherits Employee)
# Override the work() method to print:
#   -> "Developer is writing code"

# Tester (inherits Employee)
# Override the work() method to print:
#   -> "Tester is testing the application"

# Create a list of employees that contains:
# Employee(), Developer(), Tester()

# Loop through the list and call the work() method for each object to demonstrate polymorphism.

'''
class Employee:

    def work(self):
        return "Employee is working"
    
class Developer(Employee):   # Inherits Employee
    def work(self):
        return "Developer is writing code"
    

class Tester(Employee):      # Inherits Employee
    def work(self):
        return "Tester is testing the application"

employees = [Employee(), Developer(), Tester()]

for emp in employees:
    print(emp.work())
'''
#------------------------------------------------------------------------------------------------
# Q6. super() + overriding
# Create a parent class Animal with a method sound() that prints a generic message.
# Then create a child class Dog that:
# -> Overrides the sound() method
# -> Prints “Dog barks”
# -> Also calls the parent class version using super().sound()
# Finally, create an object of Dog and call its sound() method.

'''
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")
        super().sound()     # if Animal class name changed to LivingBeing code still works due to super().
        # Animal.sound(self)  # Animal → LivingBeing, this line becomes invalid.
d = Dog()
d.sound()

'''
#--------------------------------------------------------------------------------------------
# Q7. Multiple inheritance + MRO
# Create classes:
# A → method show()
# B → method show()
# C(A, B) → call show()
# Observe which method runs (MRO).

'''
class A:

    def show(self):
        print("A show method")

class B:

    def show(self):
        print("B show method")

class C(A, B):
    pass

c = C()
c.show()
'''
#--------------------------------------------------------------------------------------------
# Q.8 Abstract Class Polymorphism
# Create abstract class Shape:
# abstract method area()
# Create subclasses:
# Rectangle
# Triangle
# Use polymorphism to print areas of both.

'''
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self, l, b):
        pass                # abstraction: only method declaration

class Rectangle(Shape):

    def area(self, l, b):
        return l*b
    
class Triangle(Shape):

    def area(self, l, b):
        return (l * b) / 2
    
# polymorphism
shapes = [Rectangle(), Triangle()]

for s in shapes:
    print("Area:",s.area(2, 3))

'''
#--------------------------------------------------------------------------------------------

# 🔥 ADVANCED-LEVEL QUESTIONS (for mastery)
# Q.9 Create a class Point that represents a point in 2D space with coordinates (x, y).
# Tasks:
# Define a constructor to initialize x and y.
# Overload the + operator so that adding two Point objects returns a new Point whose coordinates are the sum of the corresponding coordinates.
# Example:
# Point(2, 3) + Point(4, 1) → Point(6, 4)
# Overload the == operator to compare two points.
# It should return True if both x and y coordinates are equal, otherwise False.

# Expected Output Example:
# p1 = Point(2, 3)
# p2 = Point(2, 3)
# p3 = p1 + p2   # Should be Point(4, 6)
# p1 == p2       # Should be True

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
#     def __eq__(self, other):
#         return (self.x, self.y) == (other.x, other.y)
        
#     def __str__(self):
#         return f"({self.x}, {self.y})"
        
# p1 = Point(2,3)
# p2 = Point(2,3)

# p3 = p1 + p2
# print(p3)
# print(p1==p2)

#--------------------------------------------------------------------------------------------
# Q.10 Operator Overloading: __str__ and __repr__

# Problem Statement:
# Create a class named Book with the following requirements:
# The class should have attributes:
# title
# author
# price
# Override the __str__() method to return a user-friendly string representation of a book.
# Override the __repr__() method to return a developer-friendly (unambiguous) string representation of a book.
# Create multiple Book objects and:
# Print a single book object directly.
# Print a list of book objects.
# Observe and explain the difference between the outputs produced by __str__ and __repr__


# class Book:

#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price


#     def __str__(self):
#         return f"{self.title} book by {self.author} - {self.price}"
    
#     def __repr__(self):
#         return f"Book(title ='{self.title}', author = '{self.author}', price = '{self.price}')"
    

# b1 = Book("Python Basics", "Amol", 499)
# b2 = Book("Advanced Python", "Guido", 799)

# print(b1)
# print([b1,b2])
#--------------------------------------------------------------------------------------------
# Q.11 Runtime Polymorphism using Composition
# Create a notification system that demonstrates runtime polymorphism through composition.
# Requirements:
# Create a base class NotificationSender that defines a method send(message).
# Create two subclasses:
# EmailSender → sends notifications via email
# SMSSender → sends notifications via SMS
# (Each subclass should override the send() method.)
# Create another class NotificationService:
# It should accept any sender object (EmailSender or SMSSender) via its constructor.
# It should call the sender’s send() method to deliver the notification.
# Show that changing the sender object at runtime changes the behavior without modifying NotificationService.


'''
# Base class (acts like an interface)
class NotificationSender:
    def send(self, message):
        pass


# Concrete implementation 1
class EmailSender(NotificationSender):
    def send(self, message):
        print(f"📧 Email sent: {message}")


# Concrete implementation 2
class SMSSender(NotificationSender):
    def send(self, message):
        print(f"📱 SMS sent: {message}")


# Uses composition (HAS-A relationship)
class NotificationService:
    def __init__(self, sender):
        self.sender = sender    # composition

    def notify(self, message):
        self.sender.send(message)


# -------- Runtime behavior --------

email_sender = EmailSender()
sms_sender = SMSSender()

service = NotificationService(email_sender) # can directly pass method as argument without storing in instance, NotificationService(EmailSender())
service.notify("Your order is confirmed")   # serivce.notify(message)

service = NotificationService(sms_sender)
service.notify("OTP is 123456")
'''
#--------------------------------------------------------------------------------------------
# Q.12. Polymorphism inside an Inheritance Chain
# 📌 Problem Statement
# Create a base class Person that defines a method called role().
# Then create two subclasses that inherit from Person:
# Student → overrides role() to describe a student’s role
# Teacher → overrides role() to describe a teacher’s role
# Create a list containing objects of different classes (Person, Student, Teacher).
# Use a loop to iterate over this list and call the role() method on each object.
# 👉 Even though the method call is the same (role()), each object should execute its own version of the method, demonstrating runtime polymorphism
'''
from abc import ABC, abstractmethod
class Person(ABC):
    @ abstractmethod
    def role(self):
        pass


class Student(Person):

    def role(self):
        return "Student is studying"

class Teacher(Person):

    def role(self):
        return "Teacher is teaching"
    

persons = [Student(), Teacher()]

for p in persons:
    print(p.role())
  '''  
#--------------------------------------------------------------------------------------------
# Q.13: Polymorphism with Exception Handling
# 📌 Problem Statement
# Create multiple classes, each implementing a common method that may raise different types of exceptions during execution.
# Using polymorphism, call this common method on objects of different classes inside a single loop, and handle all exceptions generically using try–except without knowing the object’s actual class.
'''
class FileManager:
    def process(self):
        raise FileNotFoundError("File doesn't exists")
    
class Divider:
    def process(self):
        return 10/0
    
class Converter:
    def process(self):
        int("abc")

files = [FileManager(), Divider(), Converter()]

for file in files:
    try:
        file.process()
    except Exception as e:
        print("Error occurred:", e)
'''
#--------------------------------------------------------------------------------------------
# Q.14: Method Overloading (Python Style)
# 📌 Problem Statement
# Create a class named Calculator with a method add() that behaves differently based on the number of arguments passed:
# If one argument is provided → return the same value
# If two arguments are provided → return their sum
# If three arguments are provided → return their sum
# Since Python does not support traditional method overloading, implement this behavior using:
# *args or Default parameter values


class Calculator:

    def add(self, *args):

        if not 1 <= len(args) <= 3:
            raise TypeError("add() supports only 1 to 3 arguments")
        
        else:
            return sum(args)
        
        # commented below also gives same output
        
        # if len(args)==1:
        #     return args[0]
        # elif len(args)==2:
        #     return sum(args)
        
        # elif len(args)==3:
        #     return sum(args)
        # else:
        #     raise TypeError("add() supports only 1 to 3 arguments")

c = Calculator()
print(c.add(10))
print(c.add(10,20))
print(c.add(10,20,30))