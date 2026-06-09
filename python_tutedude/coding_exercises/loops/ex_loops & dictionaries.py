"""
We have following dictionary containing details:

user = {
        "user_name" : "my_user",
        "password" : "test@123",
        "email" : "myuser@example.com",
        "address" : "XYZ road, 44444",
        "country" : "India"
        }

Delete the sensitive information from the dictionary present in a list
sensitive_info = ["password", "address"]

"""

user = {
        "user_name" : "my_user",
        "password" : "test@123",
        "email" : "myuser@example.com",
        "address" : "XYZ road, 44444",
        "country" : "India"
        }


# sensitive_info = ["password", "address"]

# for key in user:                        #RuntimeError: dictionary changed size during iteration
#     if key in sensitive_info:
#         user.pop(key)           
# print(user)

# to avoid runtime error run loop on list rather than dictionary
# for key in sensitive_info:   
#         print(f"Key : {key},  Value : {user[key]}")                     
#         user.pop(key)           
# print(user)


# if key is not present in dict
sensitive_info = ["password", "address", "phone"]

for key in sensitive_info:   
        if key in user:
                print(f"DELETED => Key : {key},  Value : {user[key]}")     
                user.pop(key)     
        else:
                print(f"{key} is not present in dictionary.")      
print(user)
