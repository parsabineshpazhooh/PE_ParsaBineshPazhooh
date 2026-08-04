record = 0
for i in range(1, 11):
    height = int(input("Enter height:"))
    if height > record:
        record = height
        print(record, "as record verified")
    if height < record:
        print("it is too small")
