# 🟡 Medium Level

# 1.Write a program to count how many lines are present in a given text file.
# 2.Write a program to count how many words are present in a file.
# 3.Write a program to read all lines of a file and store them in a list.
# 4.Write a program to write 5 user inputs into a file (each input on a new line).
# 5.Write a program to create a new file only if it does not already exist (use x mode).


# 1.Write a program to count how many lines are present in a given text file.
'''
f = open("sample.txt", "r")
lines = f.readlines()
print(len(lines))
'''

# 2.Write a program to count how many words are present in a file.
'''
f = f = open("sample.txt", "r")
lines = f.read()
print(len(lines))
'''

# 3.Write a program to read all lines of a file and store them in a list.
'''
f = open("sample.txt", "r")
lines = f.readlines()
print(lines)
'''

# 4.Write a program to write 5 user inputs into a file (each input on a new line).
'''
f = open("demo.txt", "a")

f.write(input("Enter 1st line: "))
f.write("\n")
f.write(input("Enter 2nd line: "))
f.write("\n")
f.write(input("Enter 3rd line: "))
f.write("\n")
f.write(input("Enter 4th line: "))
f.write("\n")
f.write(input("Enter 5th line: "))

'''
# 5.Write a program to create a new file only if it does not already exist (use x mode).

try:
    f = open("demo1.txt", "x")
    f.write("New file created")
    f.close()
except FileExistsError:
    print("File is exists")

