# 🔵 Method Overloading in Python
# In languages like Java/C++, method overloading means:
#       -> Same method name, different parameters (different signatures) in the same class.

# ❌ But in Python… =>
# -> Python does NOT support traditional method overloading.
# -> If you define the same method twice → the last one overrides the previous one.
'''
class Test:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):     # Only the second add() exists. The first one gets replaced.
        return a + b + c

t = Test()
print(t.add(2, 3, 4))    # works
# print(t.add(2, 3))       # ❌ Error: missing argument
'''
# ✅ Python-style Method Overloading (Achieved Using Default Arguments)

# Python solves this using:

# ✔ Default parameters
# ✔ Variable-length arguments (*args)

# 1️⃣ Using Default Arguments
# class Calculator:
#     def add(self, a=None, b=None, c=None):
#         if a is not None and b is not None and c is not None:
#             return a + b + c
#         elif a is not None and b is not None:
#             return a + b
#         else:
#             return a


# # Usage:

# c = Calculator()
# print(c.add(2, 3))      # 5
# print(c.add(1, 2, 3))   # 6

# 2️⃣ Using *args (Most common way)
# class Calculator:
#     def add(self, *nums):
#         return sum(nums)


# # Usage:

# c = Calculator()
# print(c.add(2, 3))            # 5
# print(c.add(1, 2, 3, 4, 5))   # 15


# This acts like true method overloading.
# Method overloading in Python is achieved using default parameters or *args, because Python does not support true compile-time overloading.

# 👉 Python does not support method overloading.
# 👉 If you write two methods with same name, only the last one is kept.
# 👉 To simulate overloading, you must use default arguments OR *args, but not both methods.