# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
#         o   Square root of the number
#         o   Natural logarithm (log base e) of the number
#         o   Sine of the number (in radians)
# 3.   Displays the calculated results.


# code-

import math
# Asking the user for a number as input.
number = int(input("Enter a number: "))

# Square root of the number
square = math.sqrt(number)

# Natural logarithm (log base e) of the number
log = math.log(number)

# Sine of the number (in radians)
sine = math.sin(number)

print(f"Square root: {square}")
print(f"Logarithm: {log}")
print(f"Sine: {sine}")