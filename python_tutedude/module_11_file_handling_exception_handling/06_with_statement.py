# Without -- with statement reading file=>
# read()
'''
file_handler = open("practice.txt", "rt")
read_file = file_handler.read()
print(read_file)        
file_handler.close()            # here we have to manually close the file.
'''

# With -- with statement =>

# read()
'''
with open("practice.txt", "rt") as file_handler:
    contents = file_handler.read()
# file closed automatically.
print(contents)
'''

#write()
'''
with open("practice_2.txt", "wt") as file_handler:
    file_handler.write("This creates new file with statement.\n")
    file_handler.write("File will get automatically closed.")
# file closed automatically.
'''
