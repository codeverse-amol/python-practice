# User defined functions in Python

# syntax:
# def function_name(parameters):    
#     """docstring"""
#     function_body 
#     return value

# Example 1: greeting function
def greet(name):

    print(f"Hello {name}, Good morning!!")
    print("Today is Sunday.")

greet("John")
greet("Jack")
greet("Sam")



# Example 2: adding 2 numbers

def add(a,b):
    print(a+b)

add(3,4)
add(3,0)
add(7,1)



# Example 3: checking even or odd

def even_or_odd(number):

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

even_or_odd(10)
even_or_odd(5)
even_or_odd(0)
even_or_odd(8)
even_or_odd(3)
