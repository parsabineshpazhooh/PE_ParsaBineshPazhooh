user = input("Enter your username:")
password = input("Enter password:")
counter = 0
while counter < 4:
    entered_user = input("Enter your username:")
    entered_password = input("Enter your password:")
    if entered_user == user and entered_password == password:
        print("Login Successful")
    elif entered_user != user or entered_password != password:
        print("Wrong username or password")
        counter += 1
        print("remaining chances: ", 3 - counter)

print("Finished")

