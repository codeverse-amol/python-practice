# x mode => creating a file

new_file = open("file_1.txt", "xt")

str = "Creating a new file, just for learning purpose."

# writing into file
# write(content)
new_file.write(str)
print(new_file)

# close the file
new_file.close()
# new_file.write("Add next line")          # ValueError: I/O operation on closed file.