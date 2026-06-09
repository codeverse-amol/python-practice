# Level 2 – Medium
#============================================================================
# Problems =>
#============================================================================
# 1.Write a function safe_int() that:
#   Takes user input
#   Returns integer
#   If invalid, returns: "Invalid number!"

# 2.Create a list and write code to access an index.
#   Handle IndexError

# 3.Convert a dictionary key to value.
#   Handle KeyError if key doesn't exist

# 4.Accept age and raise your own exception if age < 0.

#============================================================================
# Answers =>
#============================================================================

# 1.Write a function safe_int() that:
#   Takes user input
#   Returns integer
#   If invalid, returns: "Invalid number!"
'''
def safe_int():

    try:
        n = int(input("Enter a number: "))
        return n

    except ValueError:
        return "Invalid number!"

result = safe_int()
print(result)
'''
#------------------------------------------------------------------------------
# 2.Create a list and write code to access an index.
#   Handle IndexError
'''
my_list = [1, 2, 3, 4, 5]

try :
    index = my_list[10]
    print(index)

except IndexError:
    print("Index out of range!")
  '''  
#------------------------------------------------------------------------------
# 3.Convert a dictionary key to value.
#   Handle KeyError if key doesn't exist
'''
my_dict = {'id':101, 'name':'John', 'country':'India'}
try :
    swapped_my_dict = {v: k for k , v in my_dict.items()}       #This is a dictionary comprehension, and it is used to swap keys and values in a dictionary.
    print(swapped_my_dict['id'])
except KeyError:
    print("This key is not available!")
'''
#------------------------------------------------------------------------------
# 4.Accept age and raise your own exception if age < 0.

try:
    age = int(input("Enter the age: "))

    if age <= 0:
        raise ValueError("Age should not be negative or zero.")

    elif age >= 18:
        print("You can vote.")

    else:
        print("You are not eligible for vote!")

except ValueError as e:
    print("Error:", e)
#------------------------------------------------------------------------------