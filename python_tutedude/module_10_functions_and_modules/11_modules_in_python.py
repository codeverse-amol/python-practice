# What is a Module in Python?
# A module in Python is simply a file that contains Python code (functions, variables, classes, etc.) and has a .py extension.

# Built-in modules
# math, random, datetime,...........

# Modules help us:
# -> organize code
# -> reuse code
# -> avoid rewriting the same functions again

# how to import module in python
# syntax: import module_name

# How to Import Modules
# 1. Basic Import
# import math
# print(math.sqrt(25))

# 2. Import with Alias
# import math as m
# print(m.sqrt(25))

# 3. Import Only Specific Functions
# from math import sqrt, pi
# print(sqrt(16))

# 4. Import Everything (not recommended)
# from math import *
# print(sin(1))



## -------------In detail--------------##

import math
# Calculate square root of number

num = 100
output = math.sqrt(num)     # module.func_name(arg1, arg2,...)
print(f"Square root of {num} is {output}")

# Calculate the area of circle
r = 5
area = math.pi*r**2

print(f"The area of circle is {area} with radius {r}")
print(f"The area of circle is {area:.2f} with radius {r}")          # only takes 2 decimal values
print(math.pi)
print(f"{math.pi:.2f}")



# syntax for importing only few functions/variables: from module_name import f1, f2, f3

from random import randint

value = randint(1, 6)           # like range gives one value from 1 to 6.
print(value)



# syntax to create an alias for the module that is imported: import module_name as alias_name

import datetime as dt           # just like renaming module to use as easy in code

t = dt.time(8, 11, 20)
print(t)



# importing os module
# os
import os
print(os.getcwd()) # gets current directory