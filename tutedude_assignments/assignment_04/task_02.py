# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.



# code:

# text_write  = input("Enter text to write to the file: ")
# text_append = input("Enter additional text to append: ")

with open("output.txt", "a") as f:
    f.write(input("Enter text to write to the file: "))
    print("Data successfully written to output.txt.")
    f.write("\n")
    f.write(input("\nEnter additional text to append: "))
    print("Data successfully appended.")

with open("output.txt", "r") as f:
    print("\nFinal content of output.txt:")
    final_content = f.read()
    print(final_content)

