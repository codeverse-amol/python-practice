# calculates simple interest based on principal, rate, and time


# S.I. = Simple Interest
# P = Principal amount (the initial sum of money)
# R = Annual interest rate (in percent)
# T = Time period (in years) 

# SI = (P * R * T)/100


P = int(input("Enter the Principal amount: "))
R = int(input("Enter the Annual interest (in %): "))
T = int(input("Enter the Time period (in years): "))

SI = (P * R * T)/100

print(f"Calculated Simple Interest is {SI}.")