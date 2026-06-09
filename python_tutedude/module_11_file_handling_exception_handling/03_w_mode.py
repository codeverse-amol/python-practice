# w - mode => open the file for writing. Overwrites the file.
# if file doesn't exist, it will create new file.

fh = open("file_1.txt", "wt")
fh.write("This file is overwritten by mode 'w'\n")
fh.write("Close the file.")

fh.close()
          
