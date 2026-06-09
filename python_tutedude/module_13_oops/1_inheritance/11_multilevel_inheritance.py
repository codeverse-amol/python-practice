# Multilevel inheritance

# Multilevel inheritance means the one class inherits from another class, and then another class inherits from that derived class.
# It's forms chain of inheritance.

# 📘 Structure:
#               Class A  →  Class B  →  Class C  
#               (Base)      (Child)     (Grandchild)

# Class C gets features of both B and A.



class Grandfather:

    def property(self):
        print("Grandfather have it's own property.")

class Father(Grandfather):

    def business(self):
        print("Father have it's own business and grandfather's property too.")

class Son(Father):

    def career(self):
        print("Son have carrer, but he can do father's business and have grandfather's property too.")


s = Son()
print(s.property())  # From GrandFather
print(s.business())  # From Father
print(s.career())    # From Son



# 🧠 How It Works
# ✔ Class Son inherits from Father
# ✔ Class Father inherits from GrandFather

# Therefore, Son gets access to:

# property() → from GrandFather
# business() → from Father
# career() → from Son

# This is why Son can use all three methods.


# 📌 Real-life Analogy:

# Think like a family generation:
    # GrandFather → Father → Son

# The Son automatically gets:
    # Traits from GrandFather
    # Traits from Father
    # His own traits


# 🎯 When to Use Multilevel Inheritance?
# Use it when your data naturally fits in a hierarchy:

# Examples:
    # Vehicle → Car → ElectricCar
    # Animal → Mammal → Dog
    # Employee → Manager → SeniorManager