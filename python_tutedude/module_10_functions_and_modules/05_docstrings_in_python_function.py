# Docstrings in Python Functions

# A docstring is a special type of string that is used to document a function, class, or module in Python. It provides a convenient way to associate documentation with your code.
# Why use docstrings?
# --> To explain what the function does
# --> To describe the parameters and return values
# --> To make it easier for others (or yourself in the future) to understand the code


# Example of a function with a docstring
def add(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    a (int or float): The first number
    b (int or float): The second number

    Returns:
    int or float: The sum of a and b
    """
    return a + b

# Accessing the docstring
print(add.__doc__)


# Example of a function without a docstring
def subtract(a, b):
    return a - b
# Accessing the docstring of a function without a docstring will return None
print(subtract.__doc__)