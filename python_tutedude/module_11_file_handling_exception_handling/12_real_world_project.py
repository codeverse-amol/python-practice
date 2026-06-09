# Create 30 .txt files for 30 days study challenge
# Each file containe the day number

# import os


# path = r"C:\Users\Amol Bandgar\Desktop\Python\study_plan\30_days_challenge"

# # Create a directory to store the files

# directory = "30_days_challenge"
# if not os.path.exists(directory):
#     os.makedirs(directory)
    
# for day in range(1, 31):
#     file_path = os.path.join(directory, f"day_{day}.txt")
#     with open(file_path, "w") as file:
#         file.write(f"Day {day} study challenge")
# print(f"Created 30 files in the '{directory}' directory.")

# # Read and print the content of each file
# for day in range(1, 31):
#     file_path = os.path.join(directory, f"day_{day}.txt")
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)


import os

# ----------------------------------
# 👉 CHANGE THIS to your desired path
base_path = r"C:\Users\Amol Bandgar\Desktop\Python\study_plan\30_days_challenge"
# ----------------------------------

# Create folder
os.makedirs(base_path, exist_ok=True)

# Create 30 text files
for day in range(1, 31):
    file_path = os.path.join(base_path, f"day_{day}_task.txt")
    with open(file_path, "w") as f:
        f.write(f"Study Challenge - Day {day}\n\nTasks:\n1.\n2.\n3.\n")

print("30 .txt files created successfully!")

# Create 30 .py files
for day in range(1, 31):
    file_path = os.path.join(base_path, f"day_{day}_solution.py")
    with open(file_path, "w") as f:
        f.write(f"Study Challenge - Day {day}\n\n# Write your code here\n")

print("30 .py files created successfully!")
