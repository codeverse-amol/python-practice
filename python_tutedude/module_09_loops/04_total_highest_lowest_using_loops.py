# total_highest_lowest_using_loops

numbers = [10, 15, 5, 8, 20, 3]

total = 0
for n in numbers:
    total += n

highest = numbers[0]
for n in numbers:
    if n > highest:
        highest = n
        print(f"{n} is greater than {highest}")
    else: 
        print(f"{n} is not greater than {highest}")

lowest = numbers[0]
for n in numbers:
    if n < lowest:
        lowest = n
        print(f"{n} is less than {lowest}")
    else:
        print(f"{n} is not less than {lowest}")

print(f"Total: {total}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")