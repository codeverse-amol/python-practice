# function as an argument

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def operate(func, x, y):
    return func(x, y)
result1 = operate(add, 5, 3)
print(f"Addition result: {result1}")  # Output: Addition result: 8

result2 = operate(subtract, 5, 3)
print(f"Subtraction result: {result2}")  # Output: Subtraction result: 2

