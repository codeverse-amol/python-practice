# 🔵 Advanced Level

# 1.Write a program to copy content from file1.txt to file2.txt.
# 2.Write a program that reads a file and prints only unique words.
# 3.Write a program that reads a CSV-like file and prints each entry in a formatted manner.
# 4.Write a program to remove all blank lines from a file.
# 5.Write a program that counts occurrences of every character in a file.



# 1.Write a program to copy content from file1.txt to file2.txt.
# 🔹 File Copying
# Copy file (contents only)
# shutil.copy('source.txt', 'destination.txt')

# Copy file with metadata (permissions, timestamps)
# shutil.copy2('source.txt', 'destination.txt')
'''
import shutil

# f1 = open("file1.txt", 'r')
# f2 = open("file2.txt", 'r')

# f1.write("This is file_1.")
# f2.write("This is file_2.")

shutil.copy2("file1.txt", "file2.txt")
'''


# 2.Write a program that reads a file and prints only unique words.
'''
f1 = open("file1.txt", 'r')

lines = f1.read()
words = lines.split()           # convert text into list of words
unique_words = set(words)       # remove duplicates

print(unique_words)

f1.close()

'''

# 3.Write a program that reads a CSV-like file and prints each entry in a formatted manner.
'''
with open("data.csv", "r") as f:
    for line in f:
        name, age, city = line.strip().split(",")
        print(f"Name: {name} | Age: {age} | City: {city}")

'''

# 4.Write a program to remove all blank lines from a file.
'''
with open("sample.txt", "r") as f:
    lines = f.readlines()

with open("sample.txt", "w") as f:
    for line in lines:
        if line.strip() != "":
            f.write(line)
'''

# 5.Write a program that counts occurrences of every character in a file.
'''
f1 = open("file1.txt", 'r')

lines = f1.read()

count = {}
for ch in lines:
    if ch in count:
        count[ch] += 1

    else:
        count[ch]= 1
print(count)

f1.close()'''