# 'a' mode => Appending a file
# If file doesn't exists, it will create new.


fh = open("file_2.txt", "at")
fh.write("This file is appends new content to existing using 'a' mode.\n")
fh.write("If file doesn't exits it creates new file.")
fh.write("Good bye, tata!!")


fh.close()
          
