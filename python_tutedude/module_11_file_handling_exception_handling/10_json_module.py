# JSON Module in Python

# JSON = JavaScript Object Notation
# Used for: storing & transferring data (APIs, config files, etc.)

# Python has a built-in module called json to work with JSON data.

# 🟩 Most Important Functions
# Function	                         Meaning
# json.dumps(obj)	            Python → JSON (string)
# json.dump(obj, file)	        Python → JSON (file)
# json.loads(json_string)	    JSON string → Python
# json.load(file)	            JSON file → Python


# ✅ Common Operations
# 1. Convert Python → JSON (Serialization)

# json.dumps() → converts Python object to JSON string
# json.dump() → writes JSON data directly into a file

# Example:
import json

employee = {"id":101, "name":"John", "Company":"Dell", "Value": True} 

# converts Python object to JSON string
# jd = json.dumps(employee)
# print(jd)

# writes JSON data directly into a file
with open("emp.json", "w") as f:
    json.dump(employee, f, indent=4)        # indent writes spaces in json file.


# 2. Convert JSON → Python (Deserialization)

# json.loads() → convert JSON string to Python object
# json.load() → read JSON from a file 

# Example:
# import json

# employee = '{"id":101, "name":"John", "Company":"Dell"}'  # json string always in single quote.

# convert JSON string to Python object
# json_d = json.loads(employee)
# print(json_d)

# read JSON from a file
with open("emp.json", "r") as f:
    json_data = json.load(f)
    print(json_data)



# 🟪 Supported JSON ↔ Python Conversion
# JSON	                Python
#------------------------------
# object	            dict
# array	                list
# string	            str
# number	          int/float
# true	                True
# false	                False
# null	                None
#------------------------------