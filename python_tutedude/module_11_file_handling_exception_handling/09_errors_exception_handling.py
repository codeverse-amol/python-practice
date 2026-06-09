# Compile time error => Syntax Error & Indentation Error
# Exceptions => Errors during execution.

# How to handle exceptions => try-except block.



# result = inp_1/inp_2          # but if we take inp_2 as 0 , it throws ZeroDivisionError.
# print(result)

# To handle this type of errors exception handling comes in picture.

try:   
# try block contains the code we want to run  
    inp_1 = int(input("Enter a first number: "))
    inp_2 = int(input("Enter a second number: "))                   
    result = inp_1/inp_2
    print(result)
# If try block have any error, except block will get execute as it handles the exception.   
except ZeroDivisionError:
    print("Denominator Cannot be zero")

except ValueError:
    print("Invalid Input!")