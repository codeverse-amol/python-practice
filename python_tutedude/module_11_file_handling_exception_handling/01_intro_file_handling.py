# 📌 Introduction to File Handling in Python

# File handling means reading from and writing to files using Python.
# Whenever you want to store some data permanently (not just during program run), you use files.
# Python makes file operations very easy using the built-in open() function.

# Python provides a built-in function:

# open() function
# open(file_name, mode)

# File Modes :
# Mode	    Meaning                                 Description
# "r"	    Read	                     Opens file for reading (file must exist)
# "w"	    Write	                     Creates a new file / overwrites existing
# "a"	    Append                       Adds content at end of file
# "x"	    Create                       Creates new file, error if exists
# "r+"	    Read + Write	             Read and write, file must exist
# "w+"	    Write + Read	             Overwrites, then allows reading
# "a+"	    Append + Read	             Writes to end + allows reading




# 📌 Basic Steps of File Handling
# 1️⃣ Open the file
f = open("demo.txt", "r")

# 2️⃣ Perform operation (read/write/append)
content = f.read()

# 3️⃣ Close the file
f.close()

# ✔️ Reading a File
# Read entire file
f = open("demo.txt", "r")
print(f.read())
f.close()

# Read first 5 characters
f = open("demo.txt", "r")
print(f.read(5))
f.close()

# Read line by line
f = open("demo.txt", "r")
print(f.readline())
f.close()

# Loop through each line
f = open("demo.txt", "r")
for line in f:
    print(line)
f.close()

# ✍️ Writing to a File
# Overwrite file
f = open("demo.txt", "w")
f.write("Hello Python")
f.close()

# Append to file
f = open("demo.txt", "a")
f.write("\nThis is new line")
f.close()

# ✔️ Reading & Writing Together
f = open("demo.txt", "r+")
print(f.read())
f.write("\nAdding new text")
f.close()



# 🚀 Using with (Best Practice)
# Python automatically closes the file.

# with open("demo.txt", "r") as f:
#     print(f.read())


# 🗑️ Delete a File

# import os
# os.remove("demo.txt")