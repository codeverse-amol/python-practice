# 🧩 STRING OPERATIONS PRACTICE QUESTIONS
# 🔹 Level 1: Basic

# Count the number of characters in a string.
# Take a string input and print each character on a new line.
# Convert a string to uppercase and lowercase.
# Remove all spaces from a string.
# Check if the string starts with “Hello”.
# Find the length of a given string without using len().
# Concatenate two user-input strings and print the result.
# Find the first and last character of a string.
# Check if a string contains a specific word.
# Replace all spaces in a string with a hyphen (-).


# ---------------
# Count the number of characters in a string.

# s1 = "Hello class, we are learning python from today."
# print(len(s1))

# ---------------
# Take a string input and print each character on a new line.

# str_1 = input("Enter the string: ")

# for ch in str_1:
#     print(ch)

# other method:
# i = 0
# while i < len(str_1):
#     print(str_1[i])
#     i += 1

# ---------------
# Convert a string to uppercase and lowercase.

# str_1 = input("Enter the string: ")

# print(str_1.upper())
# print(str_1.lower())

# ---------------
# Remove all spaces from a string.

# s = " Hello world   "
# print(s.strip())

# ---------------
# Check if the string starts with “Hello”.
# s1 = "Hello class, we are learning python from today."
# print(s1.startswith("Hello"))

# ---------------
# Find the length of a given string without using len().
# s = "Hello world"
# count = 0
# for ch in s:
#     count += 1
#     print("Length of string:",count)

# ---------------
# Concatenate two user-input strings and print the result.

# user1 = input("Enter first user name:")
# user2 = input("Enter second user name:")

# result = user1 +" "+ user2
# print(result)

#---------------------
# Find the first and last character of a string.
# s1 = "Hello class, we are learning python from today"

# print(f"first char of string is \'{s1[0]}\' \nand last char of string is \'{s1[-1]}\'")

#---------------------
# Check if a string contains a specific word.
# s1 = "Hello class, we are learning python from today"

# print("Hello" in s1)
# print("python" in s1)
# print("java" in s1)

#---------------------
# Replace all spaces in a string with a hyphen (-).
# s1 = "we are learning python from today"

# print(s1.replace(" ", "-"))
