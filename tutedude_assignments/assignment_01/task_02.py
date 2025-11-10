# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.


# code:

first_name = input("Enter user's first name: ")
last_name = input("Enter user's last name: ")

full_name = first_name +" "+ last_name

print(f"Hello, {full_name}! Welcome to the Python program.")