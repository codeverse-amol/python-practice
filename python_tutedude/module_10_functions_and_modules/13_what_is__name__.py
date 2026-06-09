# In Python, __name__ is a special built-in variable that tells you how the current file is being executed.

# ✅ Quick Explanation-

# Every Python file has a variable called __name__.
# If the file is run directly, then
# __name__ == "__main__"

# If the file is imported as a module, then
# __name__ == "filename"

# ✅ Why is it useful?
# It helps you write code that runs only when the file is executed, not when it is imported.


# Example:

# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     print(add(10, 20))

# ✔ When you run this file directly
# The condition becomes true, so it prints 30.

# ✔ When someone imports this file

# Example:

# import myfile
# Then:

# The add() function becomes available
# But the print(add(10, 20)) won’t run
# (because __name__ is "myfile", not "__main__")


# 🔥 Why do we need this?
# To avoid unwanted code running during import.


# 💡 Summary
# How file is used	Value of __name__
# Run directly	"__main__"
# Imported	File name