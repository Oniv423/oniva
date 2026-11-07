import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_action = ["rock","paper","scissors"]
    computer_action = random.choice(possible_action)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            