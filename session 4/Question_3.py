import string
letters = string.ascii_letters
numbers = string.digits
password = input("Enter a password: ")
if len(password) == 8:
    if password[0:4].isascii() and password[4:7].isalnum():
        print("Password is valid")
    else:
        print("Password is not valid")
else:
    print("Password is not valid")
