# lambda function-
# A lambda function is a small, anonymous (nameless) function written in one line.

# Syntax: lambda arguments: expression

# Important:
# No def
# No function name
# Only one expression, no multiple lines


# Example 1: Simple lambda

double = lambda x: x * 2
print(double(5))


# Output: 10

# Example 2: Lambda with two parameters

add = lambda a, b: a + b
print(add(3, 4))


# Output: 7

# Example 3: Sorting using lambda

names = ["Ellon", "Jack", "Rocky", "John"]
names.sort(key=lambda x: len(x))
print(names)



# When to use lambda?

# Use lambda when the function is:
# -> Simple
# -> Used only once
# -> Fits in one line
# -> Mainly with filter(), map(), reduce(), sort()


# When NOT to use lambda?

# If your logic needs:
# -> Multiple lines
# -> Conditions
# -> Loops
# -> Print statements
# ➡️ Use normal def function.