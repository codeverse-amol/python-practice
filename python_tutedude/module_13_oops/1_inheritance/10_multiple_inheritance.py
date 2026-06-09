# Multiple inheritance

# Multiple inheritance means class can inherit from more than one parent class.


# Simple example:

class Father:
    def show_father(self):
        print("This is Father class")

class Mother:
    def show_mother(self):
        print("This is Mother class")

class Child(Father, Mother):
    pass

# class father can only access class father method
a = Father()
a.show_father()

# class mother can only access class mother method
b = Mother()
b.show_mother()

# The child inherits both methods—that’s multiple inheritance!
c = Child()
c.show_father()
c.show_mother()


# ✔ Output:
# This is Father class
# This is Mother class




# ⚠️ Diamond Problem (Important Concept)
# This happens when two parent classes inherit from the same class:

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):      # B → C , b will execute first
    pass

d = D()
d.show()

# ✔ Output:
# B

# Python uses MRO (Method Resolution Order) — it checks methods from left to right.
# Check order:
    # D → B → C → A

# Since B has show(), it is executed.

print(D.mro())     # MRO (Method Resolution Order), execution order.