# calculate the compound interest 

# formula:

# A = P*(1 + r/100)**t
# Compound Interest (CI) = A - P
# Compound Interest (CI) = P*(1 + r/100)**t - P

# A = the future value of the investment/loan, including interest  - the amount you will have
# P = the principal investment amount (the initial deposit or loan amount) -  the amount you started with
# r = the annual interest rate (as a decimal)  
# t = the number of years the money is invested or borrowed for 



P = float(input("Principal investment amount: "))
r = float(input("Annual interest rate (in %): "))
t = float(input("Number of years the money is invested or borrowed for : "))


CI = P*(1 + r/100)**t - P

print(f"The compound interest is: {CI:.2f}")