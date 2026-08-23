import random
The_number = random.randint(1, 100)
while True:
    User_number = int(input("Enter a number: "))
    if User_number == The_number:
        print("Nice")
        break
    elif User_number > The_number:
        print("Enter a smaller number")
    elif User_number < The_number:
        print("Enter a larger number")