# recursive function in python
# A recursive function is a function that calls itself in order to solve a problem. It typically has a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.


# Example of a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120


# Example of a recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:  # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))  # Output: 55


# Example of a recursive function to calculate the sum of a list of numbers
def sum_list(lst):
    if not lst:  # Base case: empty list
        return 0
    else:  # Recursive case
        return lst[0] + sum_list(lst[1:])
    
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
