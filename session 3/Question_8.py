AllOfMoney = int(input("enter any number: "))
Deposit = int(input("Enter Money you wanna deposit:"))
if Deposit > 0:
    if Deposit > AllOfMoney:
        print("Deposit is greater than all of your money\nso you can't deposit.")
    if Deposit < AllOfMoney:
        print("Deposited", AllOfMoney - Deposit)
else:
    print("You can't Deposit a number lower than Zero")
