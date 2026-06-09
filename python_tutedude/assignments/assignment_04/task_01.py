# Task 1: Read a File and Handle Errors 

# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.


# code:

try:
    with open("sample.txt", "r") as f:
        line_1 = f.readline().strip()
        line_2 = f.readline()
        print("Reading file content:")

        print(f"Line 1: {line_1}")
        print(f"Line 2: {line_2}")


except :
    print("Error : The file 'sample.txt' was not found.")
