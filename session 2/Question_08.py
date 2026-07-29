Time = int(input("Enter the Hour: "))
if 1 <= Time < 11:
    print("Day")
elif 12 <= Time <= 16:
    print("Noon")
elif 17 <= Time <= 20:
    print("down")
elif 21 <= Time <= 23:
    print("Night")
else:
    print("Didn't sign")
