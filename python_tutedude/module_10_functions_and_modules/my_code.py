# Write a python program which manage account balance, debit and credit balance.

balance = 0

def check_balance():

    print(f"Available balance: {balance}")


def deposit():
    print("Depositing amount")
    d = int(input("Enter amount to deposit: "))
    global balance
    balance += d

    return check_balance()


def withdraw():
    print("Withdraw amount")
    w = int(input("Enter amount to withdraw: "))
    global balance
    balance -= w
    return check_balance()


print("Welcome to ABC bank")
while True:

    print("1. Check balance")
    print("2. Deposit amount")
    print("3. Withdraw amount")
    print("4. Quit")
    
    choice = int(input("Enter the choice(1-4): "))

    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        break
    else:
        print("Invalid choice!!, Re-try")
print("Thank you for banking with us!!")
