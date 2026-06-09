# reading a file.


file_handler = open("practice.txt", "rt")

# read() => 
# reads the contents of the file as str
'''
read_file = file_handler.read(15)       # this reads first 10 characters of string, and only read() will read entire file.
print(read_file)
print(type(read_file))
'''


# readline() => 
# reads the first line.
'''
line_1 = file_handler.readline()
print(f"Line 1: {line_1}")

# for reading more line: empty string also can be considered to line.
line_2 = file_handler.readline()
line_3 = file_handler.readline()        # Empty string prints
line_4 = file_handler.readline()
line_5 = file_handler.readline()
line_6 = file_handler.readline()        # Empty string prints , it can print till => line_n = file_handler.readline()

print(f"Line 2: {line_2}")
print(f"Line 3: {line_3}")
print(f"Line 4: {line_4}")
print(f"Line 5: {line_5}")
print(f"Line 6: {line_6}")

'''




# readlines() => 
# reads all lines in list
# Data type of readlines => <class 'list'>

'''
lines = file_handler.readlines()

print(f"Lines : {lines}")
print(type(lines))

# output :
# Lines : ['This is practice file.\n', 'We are learning file handling in python.\n', '\n', 'Modes : r, x, w, a, t, b  => "rt" is default mode.\n', 'End of file.\n']            # \n is part of line.
# <class 'list'>



# to print every single line in readlines()=> by using for loop

for line in lines:              # this prints line one by one from list.
    print(line) 
'''

# Closing the file => close()

file_handler.close()