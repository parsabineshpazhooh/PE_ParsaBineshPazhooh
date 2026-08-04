counter = 0
my_list = []
while counter <= 10:
    numbers = int(input("Enter number:"))
    my_list.append(numbers)
    counter += 1
    if len(my_list) == 10:
        print(sum(my_list) / 10)