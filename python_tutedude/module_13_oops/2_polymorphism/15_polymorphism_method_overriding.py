# 🔥 Polymorphism – Method Overriding (Run-Time Polymorphism)
# ✅ What is Method Overriding?

# When a child class defines a method with the SAME name, SAME parameters, SAME return type as the parent class method, it is called method overriding.
# 📌 The child method replaces (overrides) the parent method.
# 📌 Python decides at runtime which method to call → RUN-TIME Polymorphism.


# 🧠 Why Method Overriding is Used?
# To modify or extend the parent class behavior without touching parent code.
# Example:
#   -> Parent class: Shape → area()
#   -> Child class: Circle → area() (overrides)
#   -> Child class: Rectangle → area()

# Each child gives its own implementation.


# ✔️ Simple Example: Method Overriding

class Parent:
    def show(self):
        print("Parent show method")

class Child(Parent):
    # overriding the parent method
    def show(self):
        print("Child show method")

c = Child()
c.show()     # Calls child version


# 🧾 Output:
# Child show method

# ✔️ Even though Child inherits show() from Parent,
# ✔️ Python calls Child version because it overrides it.


# ⭐ Important Notes
# 1. Parent & child methods MUST have same name
# ✔️ Example: show() override show()

# 2. Child method is always preferred
# Even if we call using child object.

# 3. Used for real-world polymorphism
# One interface → many implementations.

# 🧠 Quick Summary
# Feature	                       Method Overriding
# Occurs in	                          Inheritance
# Same method name?	                    ✔️ Yes
# Same parameters?	                    ✔️ Yes
# Who executes?	                Child method replaces parent
# When decided?	                        Runtime


# 🔥 How Method Overriding is Related to Polymorphism
# ✔️ Polymorphism means:
# “One function behaves differently depending on the object that calls it.”

# ✔️ Method overriding is HOW Python achieves runtime polymorphism.


# 📌 Polymorphism = Same method name → different behavior → depending on object
# Look at this:

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")


# Now check this polymorphism:

for pet in [Dog(), Cat(), Animal()]:
    pet.sound()      # same method call, different output

# OUTPUT:
# Bark
# Meow
# Some sound

# if we create object
c = Cat()
c.sound() # it prints last method which overrides
# OUTPUT:
# Meow



# ⭐ Why is this Polymorphism?

# ✔️ We are calling same method name → sound()
# ✔️ But behavior changes depending on object Dog, Cat, Animal
# ✔️ This is possible ONLY because child classes override the method.

# 💡 So what is the exact relationship?
# 🔹 Method Overriding is the mechanism
#   -> A child class replaces parent method.

# 🔹 Polymorphism is the result
#  -> Same method call → different output at runtime.

# In one line:
#  -> Method overriding enables runtime polymorphism in Python.

# 📚 Visual Understanding
# -> Inheritance gives child class access to parent methods
# -> Overriding allows child to change those methods
# -> Polymorphism allows the same method call to behave differently for each object

# So the flow is:
# Inheritance → Overriding → Polymorphism


# 🧠 Quick Summary Table
# Concept	                    Meaning	                                                 Purpose
# Inheritance	              Child gets parent methods	                                  Reuse
# Overriding	              Child replaces parent method	                         Modify behavior
# Polymorphism	       Same method behaves differently for different objects	        Flexibility