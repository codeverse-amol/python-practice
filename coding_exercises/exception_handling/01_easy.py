# Level 1 – Easy
#============================================================================
# Problems =>
#============================================================================
# 1.Write a program that takes a number from user and handles:
#   ValueError if user enters text
# 2.Ask user to divide two numbers and handle:
#   ZeroDivisionError
# 3.Open a file demo.txt and handle:
#   FileNotFoundError

#============================================================================
# Answers =>
#============================================================================

# 1.Write a program that takes a number from user and handles:
#   ValueError if user enters text

'''
try:
    num = float(input("Enter a number: "))
    print(num)

except ValueError:
    print("Invalid Inputs, please enter a number.")

'''
#------------------------------------------------------------------------------
# 2.Ask user to divide two numbers and handle:
#   ZeroDivisionError
'''
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result  = num1 / num2
    print(result)

except ZeroDivisionError:
    print("Denominator should not be zero.")

'''
#------------------------------------------------------------------------------
# 3.Open a file demo.txt and handle:
#   FileNotFoundError
'''
try:
    with open("demo.txt", "r") as f:
        rf = f.read()
        print(rf)
except FileNotFoundError:
    print("File doesn't exist!")

 '''  
 #------------------------------------------------------------------------------ 