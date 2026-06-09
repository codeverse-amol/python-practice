countries = ["India", "America", "Russia", "Indonesia", "Iran", "China", "Israil", "Australia", "Africa", "Afganistan"]

# Count all countries startswith "A"
# Also, print all these countries as a list.

count = 0
output = []             # to collect all the filtered countries.

# for country in countries:
#     if country[0]=="A":
#         count += 1
# print(count)


# Using startswith()
for country in countries:
    if country.startswith("A"):
        count += 1
        output.append(country)
    
print(f"The number of countries starts with 'A' is: {count}")
print("list =>",output)