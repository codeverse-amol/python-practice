# using os
# os.path.exists()


file_name = "practice_2.txt" 

# import os
     
# # if file doesn't present in current directory give full path.
# # i.e => C:\Users\Amol Bandgar\Desktop\python_tutedude\module_11_file_handling_exception_handling\practice.txt

# if os.path.exists(file_name):
#     print("File exists.")

# else:
#     print("File doesn't exits.")


# by using pathlib
# pathlib.Path.exists()

from pathlib import Path

file_name = Path(r"C:\Users\Amol Bandgar\Desktop\python_tutedude\module_11_file_handling_exception_handling\practice_2.txt")

if file_name.exists():
    print("File exists, No need to create.")

else:
    print("File doesn't exits, Creating new.")   
    fh = open(file_name, 'xt')
    fh.write("Creating new file!")