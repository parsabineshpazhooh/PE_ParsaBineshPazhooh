price = int(input("Enter price you paid: "))
if price <= 500000:
    print("no sale for you :(")
elif price >= 1000000:
    print("15% sale for you :)")
elif price >= 500000:
    print("10% sale for you :)")
