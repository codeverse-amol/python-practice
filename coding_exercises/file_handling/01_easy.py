# 🟢 Easy Level

# 1.Create a text file named sample.txt and write "Hello from Python" inside it.
# 2.Write a program to read the entire content of sample.txt and print it.
# 3.Write a program to read only the first 10 characters from a file.
# 4.Write a program to read a file line by line using a loop.
# 5.Append "This is an appended line" to an existing file.



# 1.Create a text file named sample.txt and write "Hello from Python" inside it.

f = open("sample.txt", "w")
f.write("Hello from Python.\n")
f.write("This is text file\n")

# 2.Write a program to read the entire content of sample.txt and print it.
'''
f = open("sample.txt", "r")
rf = f.read()
print(rf)
'''
# 3.Write a program to read only the first 10 characters from a file.
'''
f = open("sample.txt", "r")
rf = f.read(10)
print(rf)
'''
# 4.Write a program to read a file line by line using a loop.

f = open("sample.txt", "r")

for line in f:
    print(line)

# 5.Append "This is an appended line" to an existing file.

f = open("sample.txt", "a")
f.write("This is appended line ")

f.close()