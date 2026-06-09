# ✅ LEVEL 3 — MULTIPLE INHERITANCE

# Q9. Multiple Inheritance Intro
    # Class A: method hello()
    # Class B: method world()
    # Class C inherits A and B → call both.

# Q10. Method Resolution Order (MRO)
    # Create two parent classes with same method greet().
    # Child inherits both.
    # Check which one executes.

# Q11. Real Example
    # Create:
    # Printable class → method print_info()
    # Storable class → method save()
    # Document inherits both
    # Call both methods.
#==============================================================================================================================================
# Q9. Multiple Inheritance Intro
# Class A: method hello()
# Class B: method world()
# Class C inherits A and B → call both.
'''
class A:
    def hello(self):
        print("Hello")

class B:
    def world(self):
        print("World")

class C(B, A):
    def display_both(self):
        self.hello()
        self.world()


c = C()
c.display_both()
'''

#==============================================================================================================================================
# Q10. Method Resolution Order (MRO)
# Create two parent classes with same method greet().
# Child inherits both.
# Check which one executes.
'''
class M1:
    def greet(self):
        print("Hello")
class M2:
    def greet(self):
        print("Hi")

class M3(M2, M1):
    pass

m = M3()
m.greet()
'''

# The MRO is:
# M3 → M2 → M1 → object
#==============================================================================================================================================
# Q11. Real Example
# Create:
# Printable class → method print_info()
# Storable class → method save()
# Document inherits both
# Call both methods.

class Printable:

    def print_info(self):
        print("Prints info")

class Storable:

    def save(self):
        print("Saves info")

class Document(Storable, Printable):
    pass

d = Document()
d.save()
d.print_info()
#==============================================================================================================================================