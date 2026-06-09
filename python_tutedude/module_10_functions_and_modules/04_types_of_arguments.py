# # types of arguments

# # 1. positional arguments
# # 2. default arguments
# # 3. keyword arguments
# # 4. arbitrary arguments

# # 1. Positional Arguments :
# # Positional arguments are the most common type of arguments in Python. They are passed to a function in the order they are defined. The number of arguments passed must match the number of parameters defined in the function.

# def greet(name, message):
#     print(f"{message}, {name}!")
# greet("Alice", "Hello")  # Positional arguments
# greet("Bob", "Good morning")  # Positional arguments

# # 2. Default Arguments :
# # Default arguments are parameters that have a default value. If the caller does not provide a value for that parameter, the default value will be used.
# def greet(name, message="Hello"):
#     print(f"{message}, {name}!")
# greet("Alice")  # Uses default message "Hello"
# greet("Bob", "Good morning")  # Overrides default message with "Good morning"

# # 3. Keyword Arguments :
# # Keyword arguments are passed to a function by explicitly specifying the parameter name. This allows you to pass arguments in any order.
# def greet(name, message):
#     print(f"{message}, {name}!")

# greet(name="Alice", message="Hello")  # Keyword arguments
# greet(name="Bob", message="Good morning")  # Keyword arguments


# # 4. Arbitrary Arguments :
# # Sometimes, you may want to pass a variable number of arguments to a function. In such cases, you can use arbitrary arguments. There are two types of arbitrary arguments: *args for non-keyword arguments and **kwargs for keyword arguments.
# def greet(*args):
#     for arg in args:
#         print(arg)

# greet("Hello", "Alice")  # Arbitrary arguments
# greet("Good morning", "Bob")  # Arbitrary arguments

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# greet(name="Alice", message="Hello")  # Arbitrary keyword arguments
# greet(name="Bob", message="Good morning")  # Arbitrary keyword arguments

# combining different types of arguments
def greet(name, message="Good Morning", *args, **kwargs):

    return f"""
            This is positional argument: {name}
            This is default argument: {message}
            This is multiple positional argument: {args}
            This is keyword argument: {kwargs}
"""

g = greet("Amol", "Good Afternoon", 1, 2, 3, a="keyword", b="argument")
print(g)