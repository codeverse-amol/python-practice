# read()
# while using this mode, if file doesn't exists, it gives "FileNotFoundError".
# give full path if file doesn't exist in current working directory.
# In read if we try to writw the file or vice-versa , it gives "UnsupportedOperation Error".
# But while in write mode, if use read() it gives error but --> fh = open("file_1.txt", "wt") <-- get execute and delete all content because it get overwritten empty string and then throws error.

# If file exists don't use --> 'x' mode --> FileExistsError 
                             # use 'w' mode to overwrite or 'a' mode to append.
