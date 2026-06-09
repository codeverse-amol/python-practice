# Abstraction:

# Abstraction means showing only what is neccessary and hiding implimenting details.

# This helps:
# Reduce complexity
# Writing clean, maintainable code
# Working in teams(very important in indstry)


# Real-life Example
# When you use a remote control:
# You press Power ON
# You don’t know how electricity flows inside the TV
# 👉 You use features, not internal logic


# 🐍 How Abstraction is Done in Python?
# Python provides abstraction using:
# 1️⃣ Abstract Base Classes (ABC)
# 2️⃣ @abstractmethod decorator


# These are available in the abc module.


# Example :
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def speed(self, distance, time):  
        pass


class Car(Vehicle):

    def speed(self, distance, time):
        return distance/time

class Truck(Vehicle):

    def speed(self, distance, time):
        return distance/time
    

c = Car()
t = Truck()
print(c.speed(100,2))
print(t.speed(100,3))

'''

# Abstraction is not just inheritance.
# It is enforcing a contract using @abstractmethod.

# If an abstract method is not implemented in the child class, Python prevents object creation.


# Let’s show a FULL, REAL-WORLD STYLE example step by step, exactly what happens in a team / industry project and why abstraction matters.
# Explain as if you are a new developer joining the team.

# 🔒 FULL EXAMPLE: Abstraction in a Real Project
# 🎯 Goal
# We want a system that can:
# Calculate speed of any vehicle
# Without changing common code
# Enforce rules so no developer breaks the system


# 1. Senior Developer Creates the CONTRACT (Abstract Class)
# This is usually done by a lead/senior dev.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def speed(self, distance, time):
        """
        Calculate speed of the vehicle
        
        distance: in km
        time: in hours
        """
        pass

# 🔍 What this means
# Every vehicle must have speed(distance, time)
# Parameters are fixed
# No one can skip implementation
# 👉 This is the rule book for the team.

# 2. Different Developers Implement Different Vehicles
# 🏍️ Developer A: Bike
class Bike(Vehicle):

    def speed(self, distance, time):
        return distance/time

# 🚗 Developer B: Car

class Car(Vehicle):

    def speed(self, distance, time):
        return distance/time
    
# 🚚 Developer C: Truck
class Truck(Vehicle):

    def speed(self, distance, time):
        return distance/time
    

# 3. Common Function Written ONCE (Important 🔥)
# This function is written by another team (or earlier).

def print_speed(vehicle:Vehicle):
    print("Speed:", vehicle.speed(100,2), "km/h") # or print(f"Speed: {vehicle.speed(100,2)} km/h")
    
# 🔑 Key Point
# This function:
# Does NOT know about Car / Truck / Bike
# Only knows Vehicle
# Will NEVER change even if new vehicles are added

# Using the System
b = Bike()
c = Car()
t = Truck()

print_speed(b)
print_speed(c)
print_speed(t)


# 🔥 Why This Is Powerful (Industry Perspective)
# ✅ Add new feature WITHOUT touching old code

# A new developer joins and adds a Bus.


class Bus(Vehicle):

    def speed(self, distance, time):
        return distance/time
    

bu = Bus()
print_speed(bu)




# ❌ What Happens If a Developer Makes a Mistake?

# Case 1: Forget to implement speed

# class Auto(Vehicle):
#     pass
# a = Auto()   # ❌ ERROR


# 👉 Python error:
# TypeError: Can't instantiate abstract class Auto

# ✔ Bug caught EARLY
# ✔ No runtime crash in production


# Case 2: Wrong method name

# class Taxi(Vehicle):
#     def calculate_speed(self, distance, time):
#         return distance / time

# t = Taxi()   # ❌ ERROR


# 👉 Contract violation caught immediately.


# What if I want output like:

# Speed of Car: 50.0 km/h
# Speed of Truck: 50.0 km/h
# Speed of Bike: 50.0 km/h

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def speed(self, distance, time):
        """
        Calculate speed of the vehicle
        
        distance: in km
        time: in hours
        """
        pass


    # Adding new method for name of vehicle
    @ abstractmethod
    def name(self):
        pass


class Bike(Vehicle):

    def speed(self, distance, time):
        return distance/time
    
    def name(self):
        return "Bike"


class Car(Vehicle):

    def speed(self, distance, time):
        return distance/time
 
    def name(self):
        return "Car"

class Truck(Vehicle):

    def speed(self, distance, time):
        return distance/time
    
    def name(self):
        return "Truck"
    
class Bus(Vehicle):

    def speed(self, distance, time):
        return distance/time
    
    def name(self):
        return "Bus"

def print_speed(vehicle:Vehicle):
    vs = vehicle.speed(100,2)
    print(f"Speed of {vehicle.name()} is: {vs} km/h")
    

b = Bike()
c = Car()
t = Truck()
bu = Bus()


print_speed(b)
print_speed(c)
print_speed(t)
print_speed(bu)





# 🔥 EVEN BETTER (Cleaner Design)

# Instead of name() method, use class name automatically 👇

# 🔹 Abstract class stays same
class Vehicle(ABC):

    @abstractmethod
    def speed(self, distance, time):
        pass

# 🔹 Child classes stay simple
class Bike(Vehicle):
    def speed(self, distance, time):
        return distance / time
    
class Car(Vehicle):
    def speed(self, distance, time):
        return distance / time

class Truck(Vehicle):
    def speed(self, distance, time):
        return distance / time

# 🔹 Common function (Smart ✨)
def print_speed(vehicle: Vehicle):
    name = vehicle.__class__.__name__
    sp = vehicle.speed(100, 2)
    print(f"Speed of {name}: {sp} km/h")


b = Bike()
c = Car()
t = Truck()

print_speed(b)
print_speed(c)
print_speed(t)


# ✔ Output (Same)
# Speed of Bike: 50.0 km/h
# Speed of Car: 50.0 km/h
# Speed of Truck: 50.0 km/h


# 🧠 Which Approach Should YOU Use?
# Situation	                                                                    Use
# Vehicle names are simple	                                            __class__.__name__ ✅
# Vehicle needs custom name	                                            name() abstract method
# Internationalization	                                                       name()
# Logging / analytics	                                                       name()