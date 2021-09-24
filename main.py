import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break



    if user_input not in options:
        print("Not a valid answer. ")
        continue
    random_number = random.randint(0,2)
    # rock is 0 paper is 1 scissors is 2
    computer_pick = options[random_number]
    print("Computer picked ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "rock":
        print("Tie ")
        user_wins += 1
        computer_wins += 1
    if user_input == "paper" and computer_pick == "paper":
        print("Tie")
        user_wins += 1
        computer_wins += 1
    if user_input == "scissors" and computer_pick == "scissors":
        print("Tie")
        user_wins += 1
        computer_wins += 1

    if user_input == "rock" and computer_pick == "scissors":
        print("YOU WON! ")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("YOU WON! ")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("YOU WON! ")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "scissors":
        print("You Lost.")
        computer_wins += 1
    elif user_input == "rock" and computer_pick == "paper":
        print("You Lost.")
        computer_wins += 1
    elif user_input == "scissors" and computer_pick == "rock":
        print("You Lost.")
        computer_wins += 1


print("Goodbye.")
print("You won ", user_wins, "times")
print("Computer won ", computer_wins, "times")