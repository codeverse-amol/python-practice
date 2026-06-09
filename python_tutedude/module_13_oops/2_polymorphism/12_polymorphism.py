# Polymorphism:
# Polymorphism allows one name to behave differently depending on the object.
# Polymorphism = Same name, different behavior

# ✅ Types of Polymorphism in Python
# There are 4 major types:

# Operator Overloading :
# -> Built-in operators behave differently with different data types.
# -> Example: + operator
#       print(5 + 10)          # Integer addition
#       print("Hello " + "World")  # String concatenation   
#       print([1, 2] + [3, 4])    # List concatenation
#       print((1, 2) + (3, 4))    # Tuple concatenation
#       print({1: 'a'} + {2: 'b'})  # Dictionary addition (will raise an error in Python)


# Method Overriding (Runtime Polymorphism) :
#   -> Happens in inheritance when child class gives its own version of a parent method.


# Method Overloading (Compile-time Polymorphism) — Python Style :
#   -> Python does NOT support traditional overloading,
#   -> BUT we can achieve similar behavior using:
#   -> ✔ Default arguments
#   -> ✔ Variable arguments (*args)

# Duck Typing (Python Special Polymorphism) :
#   -> “If it walks like a duck and quacks like a duck → it's a duck.”
#   -> In Python, Type doesn’t matter — only the presence of methods matters.
