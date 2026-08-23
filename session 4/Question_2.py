import random
choices = ["scissors", "paper", "rock"]
choice = input("Enter your choice number\n1) start game\n2) exit\n:")
if choice == "1":
    while True:
        Game_Choice = input("Enter rock, scissors ,paper: ").lower()
        Computer_choice = random.choice(choices)
        if Game_Choice != "scissors" and Game_Choice != "paper" and Game_Choice != "rock":
            print("WRONG CHOICE!")
        if Computer_choice == "rock" and Game_Choice == "scissors":
            print("Computer win!")
        if Computer_choice == "paper" and Game_Choice == "rock":
            print("Computer win!")
        if Computer_choice == "scissors" and Game_Choice == "paper":
            print("Computer win!")
        if Computer_choice == "rock" and Game_Choice == "paper":
            print("You win!")
        if Computer_choice == "paper" and Game_Choice == "scissors":
            print("You win!")
        if Computer_choice == "scissors" and Game_Choice == "rock":
            print("You win!")
        if Computer_choice == Game_Choice:
            print("Draw!")
if choice == "2":
    print("Finished")
