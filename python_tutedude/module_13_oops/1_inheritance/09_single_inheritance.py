# inheritance in python:
# Inheritance allows one class (child) to acquire properties & methods of another class (parent).

# It helps you:
# ✔ avoid code duplication
# ✔ reuse existing functionality
# ✔ build logical class hierarchies
# ✔ extend or customize behavior

# 1️⃣ Single Inheritance
# One parent → One child.

    # class Parent:
    #     pass

# class Child(Parent):
#     pass


# 2️⃣ Multilevel Inheritance
# Child → Grandchild.

    # class A:
    #     pass
    # class B(A):
    #     pass
    # class C(B):
    #     pass


# 3️⃣ Multiple Inheritance
# Child inherits from multiple parents.

# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

#------------------------------------------------------------------------------------------------------------
# Single Inheritance:

# In single inheritance, a child class inherits from a single parent class.
# The vehicle class is parent class/ base class

class Vehicle:

    def __init__(self, n_wheels, n_seats, mileage): # Initializer/ constructor of parent class

        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def vehicle_info(self): # method of parent class
        return f"The vehicle has {self.n_wheels} wheels, {self.n_seats} seats and mileage is {self.mileage}kmpl "
    

# v1 = Vehicle(4, 5, 15)
# print(v1.vehicle_info())


# The car class is child class/ derived class

# class Car(Vehicle): 
#     pass

# c1 = Car(4, 5, 15)
# print(c1.vehicle_info())


# Car class inherites the properties and methods of Vehicle class
# So we can create object of car class and access vehicle_info method of vehicle class.


# what if class Car has its own __init__ method?
# In that case, we need to call the __init__ method of parent class explicitly using 
# super() function.

class Bike(Vehicle):

    showroom_name = "ABC"  # class variable
    def __init__(self, bike_name): # Initializer/ constructor of child class
        self.bike_name = bike_name
        Vehicle.__init__(self, 2, 2, 20 )     # calling parent class __init__ method explicitly
        # or we can use super() function
        # super().__init__("audi", 8000000, 20)
            # here we are initializing the attributes of parent class
            # name, price, mileage

    # def vehicle_info(self):  # overriding vehicle_info method of parent class
    #     return f"The bike name is {self.bike_name}, showroom is {self.showroom_name}"   
    

b1 = Bike("Ninja")
print(b1.showroom_name) # accessing class variable of bike class
print(b1.vehicle_info()) 

# here bike class has its own __init__ method, so we need to call the parent class __init__ method explicitly
# to initialize the attributes of parent class.
# here bike class has its own vehicle_info method, so it overrides the vehicle_info method of parent class.
# If we comment the vehicle_info method of bike class, then it will call the vehicle_info method of vehicle class.

# print(b1.name)   # accessing parent class attribute
# print(b1.price)  # accessing parent class attribute 
# print(b1.mileage)  # accessing parent class attribute
# print(b1.bike_name)  # accessing child class attribute




# Single Inheritance - Arguments    

class Truck(Vehicle):
    def __init__(self, wheels, seats, mileage, load_capacity): # Initializer/ constructor of child class
        super().__init__(wheels, seats, mileage)  # calling parent class __init__ method using super()
        self.load_capacity = load_capacity  # child class attribute

    # def vehicle_info(self):  # overriding vehicle_info method of parent class
    #     parent_info = super().vehicle_info()  # calling parent class vehicle_info method using super()
    #     return f"{parent_info} and load capacity is {self.load_capacity} tons"
    
t1 = Truck(16, 2, 8, 25)
print(t1.vehicle_info())    
# here truck class has its own __init__ method with additional argument load_capacity
# so we need to call the parent class __init__ method using super() to initialize the attributes of parent class.
# here truck class has its own vehicle_info method, so it overrides the vehicle_info method of
# parent class. It also calls the parent class vehicle_info method using super() to get the parent class info.
# If we comment the vehicle_info method of truck class, then it will call the vehicle_info method of vehicle class.
# print(t1.name)   # accessing parent class attribute
# print(t1.price)  # accessing parent class attribute

# print(t1.mileage)  # accessing parent class attribute
# print(t1.load_capacity)  # accessing child class attribute


# Single Inheritance - Method Overriding 
# Method overriding is a feature of OOP that allows a child class to provide a specific implementation of a method that is already defined in its parent class.
# When a method in a child class has the same name, same parameters or signature, and same return type(or sub-type) as a method in its parent class, then the method in the child class is said to override the method in the parent class.
# When you call the method from an object of the child class, the version of the method in the child class is executed, not the one in the parent class.
# This allows for dynamic polymorphism, where the behavior of a method can be determined at runtime based on the object type.
   
class Bus(Vehicle):

    pass  # comment this pass to add vehicle_info method of bus class

    # def vehicle_info(self):  # overriding vehicle_info method of parent class
    #     return "This is a bus" 
    
b2 = Bus(6, 50, 12)
print(b2.vehicle_info())

# here bus class has its own vehicle_info method, so it overrides the vehicle_info method of parent class.
# If we comment the vehicle_info method of bus class, then it will call the vehicle_info method of vehicle class.
# print(b2.name)   # accessing parent class attribute
# print(b2.price)  # accessing parent class attribute      