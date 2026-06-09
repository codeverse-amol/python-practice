# Functions in Python :
# A function in Python is a block of reusable code that performs a specific task.
# Instead of writing the same code again and again, you can write a function once and use it multiple times.

# Why do we use functions?
# --> To avoid repeating code
# --> To make the program organized
# --> To make code cleaner and easier to understand
# --> To divide a big program into smaller chunks


# Types of Functions :

# Built-in functions     →  print(), len(), input(), sum(), etc.
# User-defined functions →  functions created by us


# Example of a built-in function
print("Hello, World!")
print(len("Hello, World!"))


# Example of a user-defined function
def first_even(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result
print(first_even([1,3,5,8,10]))



# pass by value and pass by reference :
# In Python, all variables are references to objects in memory. When you pass a variable to a function, you are passing a reference to the object, not the actual value. This means that if you modify the object inside the function, it will affect the original object outside the function.

def modify_list(my_list):
    my_list.append(4)  # This modifies the original list because my_list is a reference to the original list
my_numbers = [1, 2, 3]
modify_list(my_numbers)

print(my_numbers)  # Output: [1, 2, 3, 4] - The original list is modified because it was passed by reference



def modify_number(num):
    num += 1  # This does not modify the original number because num is a reference to an immutable object (integer)
my_num = 5
modify_number(my_num)
print(my_num)  # Output: 5 - The original number is not modified because it was passed by value (or more accurately, by object reference for immutable objects)