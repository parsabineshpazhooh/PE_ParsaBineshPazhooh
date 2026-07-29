Card_Number = input("Enter your card number: ")
if Card_Number[0:4] == "6037":
    print("This is for Melli_Bank\nso you can use that.")
elif Card_Number[0:4] != "6037":
    print("This is not for Melli_Bank\nSo you can't use that.\n\nCardNumberError")
