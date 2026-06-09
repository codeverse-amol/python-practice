# for loop with string and dictionary

# Example-1: for loop with string
'''
str1 = "hello world"

for char in str1:
    print(char)

print("Loop ends here..")
'''

# Example-1: for loop with dictionaries

dict_1 = {'id':101, 'name':'Jack', 'company':'HCL'}

# for d in dict_1:
#     # print(d)        # this print only keys.
#     # to print key:value pair
#     print(d,":",dict_1[d])  # d represents the key of the dictionary.


# using keys()- only prints keys
for d in dict_1.keys():
    print(d)

# using values()- only prints values
for d in dict_1.values():
    print(d)

# using items()- key:value pair prints by comma separated.
for d in dict_1.items():
    print(d)