all_of_money = int(input("enter any number: "))
Deposit = int(input("Enter Money you wanna deposit:"))
if Deposit > 0:
    if Deposit > all_of_money:
        print("Deposit is greater than all of your money\nso you can't deposit.")
    if Deposit < all_of_money:
        print("Deposited", all_of_money - Deposit)
else:
    print("You can't Deposit a number lower than Zero")
