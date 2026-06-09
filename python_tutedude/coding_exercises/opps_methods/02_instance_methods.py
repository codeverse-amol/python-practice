# ✅ 2. PRACTICE QUESTIONS — INSTANCE METHODS

# Q1. Create a class Laptop with brand, RAM, price.
# Write instance methods:
# upgrade_ram()
# apply_discount()
# show_details()

# Q2. Create class Cart with a list of items.
# Add instance methods:
# add_item()
# remove_item()
# total_items()

# Q3. Make a class Counter with instance variable count=0.
# Methods:
# increment()
# decrement()
# reset()

# Q4. Create Movie class with name, rating.
# Write method update_rating().

# Q5. Create Temperature class with Celsius.
# Instance method to convert to Fahrenheit.
#----------------------------------------------------------------------------

# Q1. Create a class Laptop with brand, RAM, price.
# Write instance methods:
# upgrade_ram()
# apply_discount()
# show_details()

# Solution:
# class Laptop:

#     def __init__(self, brand, RAM, price):
#         self.brand = brand
#         self.ram = RAM
#         self.price = price
#         self.selling_price = price   # will update after discount

#     def upgrade_ram(self, extra_ram):
#         self.ram += extra_ram
#         self.price += 10000

#     def apply_discount(self, discount_percentage):
#         discount_amount = self.price * (discount_percentage)/100
#         self.selling_price = self.price - discount_amount
        
#     def show_details(self):
#         print(f"Laptop Brand       : {self.brand}")
#         print(f"RAM After Upgrade  : {self.ram:.2f} GB")
#         print(f"Original Price     : {self.price:.2f}")
#         print(f"Final Selling Price: {self.selling_price:.2f}")

# l1 = Laptop("Dell", 16, 750000)
# l1.upgrade_ram(16)
# l1.apply_discount(10)
# l1.show_details()
#----------------------------------------------------------------------------

# Q2. Create a class Cart that stores a list of items.

# The class should have the following instance methods:
# 1️⃣ add_item(item)
# Adds the given item into the cart.

# 2️⃣ remove_item(item)
# Removes the given item from the cart (if it exists).

# 3️⃣ total_items()
# Returns or prints the total number of items present in the cart.


# Solution:

# class Cart:

#     def __init__(self):
#         self.items = []  # each cart has its own list of items
    
#     def add_item(self, item):
#         self.items.append(item)
#         print(f"{item} added successfully")
   

#     def remove_item(self, item):

#         if item in self.items:
#             self.items.remove(item)
#             print(f"\n{item} removed successfully.") 
#         else:
#             print(f"\n{item} not found in cart.")        

#     def total_items(self):

#         print(f"\nTotal items in cart: {len(self.items)}")
#         print("Items:", self.items)


# i = Cart()

# i.add_item("Bread")
# i.add_item("Cheese")
# i.add_item("Milk")

# i.remove_item("Biscuit")
# i.total_items()

#----------------------------------------------------------------------------
# Q3. Create a class named Counter that keeps track of a numeric count.

# ✔ Requirements
# Instance Variable

# count → initialized to 0 for every new object.
# Methods
# increment()
# Increases the value of count by 1.

# decrement()
# Decreases the value of count by 1.
# (You may optionally prevent negative values.)

# reset()
# Resets the value of count back to 0.



# Solution:

# class Counter:

#     def __init__(self, count=0):
#         self.count = count      

#     def increment(self):
#         self.count += 1
#         print(f"Count after increment: {self.count}")

#     def decrement(self):
#         if self.count > 0:
#             self.count -= 1        
#             print(f"Count after decrement: {self.count}")
#         else:
#             print("Invalid decrement!!")

#     def reset(self):
#         self.count = 0
#         print(f"The count after reset is {self.count}")


# c1 = Counter()      # starts at 0 automatically
# c1.increment()      # Count = 1
# c1.increment()       # Count = 2    
# c1.decrement()      # Count = 1    
# c1.reset()          # Count = 0


#----------------------------------------------------------------------------

# Q4. Create a Movie class that contains two attributes:
# name
# rating
# Write an instance method update_rating() that updates the movie's rating to a new value.


# Solution:

# class Movie:

#     def __init__(self, name, rating):
#         self.name = name
#         self.rating = rating

#     def update_ratings(self, new_rating):
#         self.rating = new_rating
#         print(f"Updated rating is: {self.rating}")


# m = Movie("Ranjhana", 9.8)
# m.update_ratings(9.9)

#----------------------------------------------------------------------------
# Q5. Create a Temperature class that stores a temperature value in Celsius.
# Write an instance method that converts the Celsius value to Fahrenheit and returns the result.
# formula : F = (C × 9/5) + 32


# Solution:

# class Temperature:

#     def __init__(self, temp_c):
#         self.temp_c = temp_c

#     def to_fahrenheit(self):
#         temp_f = int((self.temp_c * 9/5) + 32 )      # division gives float value, converted float to integer.
#         return temp_f


# t = Temperature(30)                                 # Given temperature is in celsius
# result = t.to_fahrenheit() 

# print(f"Temperature in Celsius: {t.temp_c}°C")
# print(f"Temperature in Fahrenheit: {result}°F")


