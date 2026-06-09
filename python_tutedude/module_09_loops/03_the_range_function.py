# range()- built-in function that genrates sequence of intergers, in given interval.
# Syntax: range(start, stop, step) 
# start: starting value of sequence (inclusive). Default is 0
# stop: ending value of sequence (exclusive)
# step: difference between each number in the sequence. Default is 1
# returns range object

# Example-1: Syntax: range(start, stop, step)
# prints the number from 1 to 20 with step 2.
'''
for i in range(1,20,2):
    print(i)
'''
# Example-2:
# prints the even numbers from 1 to 10 (10 excluded).
'''
for i in range(2,10,2):  # start from even with step even will get even.
    print(i)
'''
# Example-3:
# prints the odd numbers from 1 to 10 (10 excluded).
'''
for i in range(1,10,2): # start from odd with step odd will get odd.
    print(i)
'''   

# Example-3:
# reverse order ==> from 10 to 1 (1 excluded).
'''
for i in range(10, 0, -1):
    print(i)
print("Happy new year!!!")
'''


# using for sequences
'''
# Example-1:
groceries = ["sugar", "milk", "bread", "wheat"]

for items in groceries:
    print(items)

# getting indexes in range using len():

for index in range(len(groceries)):
    print(index)
'''

# Example-2:
profit = ["10%", "25%", "15%", "22%"]

for index in range(len(profit)):
    q = index + 1
    print(f"Quarter {q} profit is {profit[index]}")