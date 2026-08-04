my_str = input("Enter your string: ")
if len(my_str) % 2 == 0:
    length = len(my_str)
    print(my_str[0:length // 2:])
elif len(my_str) % 2 == 1:
    length = len(my_str)
    print(my_str[(length // 2) - 1::])
