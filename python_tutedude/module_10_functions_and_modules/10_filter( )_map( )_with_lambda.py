# filter and map function-

def filter(func, seq):
    result = []
    for item in seq:
        if func(item):
            result.append(item)
    return result

def map(func, seq):
    result = []
    for item in seq:
        result.append(func(item))
    return result


#syntax-
# filter(function, seq)
# map(function, seq)


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(filter(lambda x : True if x % 2 == 0 else False, num)))        # one-line code 
# is same as :

even = filter(lambda x : True if x % 2 == 0 else False, num)                # it will filter the even nums by using condition
print(list(even))                                                           # list collect all filtered nums values.

check_even = map(lambda x : True if x % 2 == 0 else False, num)             # map will map true for even and false for odd by using condition
print(list(check_even))                                                     # it will collect all true , false which mapped to the nums