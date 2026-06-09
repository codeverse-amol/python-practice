# Operator Overloading in Python (Part of Polymorphism)

# Operator overloading means:
# -> You can redefine how operators work for your own custom classes.
# For example: +, -, *, <, ==
# Python allows you to change their behavior using special methods (dunder methods) like:
# Operator	                 Method
# +	                        __add__()
# -	                        __sub__()
# *	                        __mul__()
# <	                        __lt__()
# ==	                    __eq__()


# Why is this Polymorphism?

# Because:
# 👉 Same operator behaves differently depending on the object
# + works for numbers, strings, lists, and now your class.

# 5 + 5  → addition
# "hi" + "bye" → concatenation
# list1 + list2 → merge
# d1 + d2 → custom logic

# same for other methods.