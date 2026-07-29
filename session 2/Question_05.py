Distance = int(input("Enter the Distance: "))
if Distance < 2:
    fare = 20000
else:
    fare = 20000 + (Distance * 5000)
print(f"last fare is {fare}")
