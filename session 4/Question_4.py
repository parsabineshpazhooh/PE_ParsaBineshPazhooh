total = 0
while True:
    x = int(input("Enter a number: "))
    if x == 0:
        print("Finish")
        break
    else:
        total += x
print(total)
