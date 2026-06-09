# 🥒 Pickle Module in Python

# The pickle module is used to serialize and deserialize Python objects.

# ✔ What is Serialization?
# Converting a Python object → byte stream (so it can be saved in a file or sent over network).

# ✔ What is Deserialization?
# Converting byte stream → original Python object.

# Pickle is basically used to store Python objects permanently.

# 📌 Why do we use pickle?

# Save Python objects to a file
# Load them back whenever needed
# Used in ML models to save trained models
# Works with any Python object: lists, dicts, sets, classes, objects, etc.


# 🔧 Important Functions in pickle
# Function	Meaning
# pickle.dump(obj, file)	Serialize object & save into file
# pickle.dumps(obj)	Serialize object & return bytes
# pickle.load(file)	Load object from file
# pickle.loads(bytes)	Deserialize bytes to object



# # 📍 Example: Save & Load Using Pickle

# # ➤ Saving (dump)
# import pickle

# data = {"name": "Amol", "age": 22, "skills": ["Python", "Git"]}

# with open("data.pkl", "wb") as f:
#     pickle.dump(data, f)




# # ➤ Loading (load)
# import pickle

# with open("data.pkl", "rb") as f:
#     result = pickle.load(f)

# print(result)




# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s = Student("Amol", 90)

# with open("student.pkl", "wb") as f:
#     pickle.dump(s, f)

# # Load
# with open("student.pkl", "rb") as f:
#     obj = pickle.load(f)

# print(obj.name, obj.marks)

#=====================================================================================#
# 📝 PART 1: Practice Questions
# ✅ Beginner Level

# What is serialization and deserialization in Python? Explain with pickle example.
# Write a program to pickle a list and load it back.
# How do pickle.dump() and pickle.load() work?
# Write code to store a dictionary in a file using pickle.
# Why do we use binary mode 'wb' and 'rb' with pickle?

#--------------------------------------------------------------------------------------
# 1. What is serialization and deserialization in Python? Explain with pickle example.

# Answer:

# Serialization
# Serialization means converting python objects into the byte stream so that it can be:
# saved into a file
# Transferred over network
# Stored for later use


# In python this is done using:
# pickle.dump(obj, file)

# Deserialization
# Deserialization means converting byte stream back into the original Python object.

# In python this is done using:
# pickle.load(file)


import pickle

# Python object
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# serialization:    python object --> bytes written into file.
with open("sample.pkl", "wb") as f:
    pickle.dump(l, f)

# deserialization:   byte --> python object.
with open("sample.pkl", "rb") as f:
    fr = pickle.load(f)
    print(fr)
#--------------------------------------------------------------------------------------
# 2. Write a program to pickle a list and load it back.

import pickle

# Python object
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open("sample.pkl", "wb") as f:
    pickle.dump(l, f)

with open("sample.pkl", "rb") as f:
    fr = pickle.load(f)
    print(fr)
#--------------------------------------------------------------------------------------

# 3. How do pickle.dump() and pickle.load() work?

# pickle.dump() and pickle.load() are used in python to serialize and deserialize the objects.

# pickle.dump():
# How it works:
# Takes input as python objects i.e list, dict, class, anything.
# Converts into byte stream.
# Write those files into file openeded in binary write mode (wb).
# pickle.dump(data, file)


# pickle.load()
# It reads the stored byte stream from file and convert back into the original python object.
# How it works:
# Reads bytes from a file opened in binary read mode (rb).
# Converts those bytes back into the same Python object (list/dict/class object).
# data = pickle.load(file)


# 🧪 Code Example (dump + load)
import pickle

data = {"name": "Amol", "age": 22}

# Serialize and save to file
with open("info.pkl", "wb") as f:
    pickle.dump(data, f)

# Deserialize and load from file
with open("info.pkl", "rb") as f:
    result = pickle.load(f)

# print(result)
#--------------------------------------------------------------------------------------
# 4. Write code to store a dictionary in a file using pickle.

import pickle

employee = {'id':101, 'name':'John', 'Company':'IBM'}

# storing dictionary in a file
with open("employee.pkl", 'wb') as f:
    pickle.dump(employee, f)

# # you can check and read your dictionary by below code
# with open("employee.pkl", 'rb') as f:
#     rf = pickle.load(f)
#     print(rf)
#--------------------------------------------------------------------------------------

# 5. Why do we use binary mode 'wb' and 'rb' with pickle?

# ans:

'''We use 'wb' and 'rb' with pickle because pickle stores data in binary format, not text.
'wb' ensures we write raw bytes to the file, and 'rb' ensures we read the same bytes back without any changes.
Using text mode would corrupt the pickle data.'''

#--------------------------------------------------------------------------------------