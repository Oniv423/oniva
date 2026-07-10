import random
attempts_list = []
def show_score():
    if len(attempts_list)<= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int (random.radiant(1, 10))
    print("Hey There! Welcome to the game of guesses!")
    player_name = input("Enter your name!")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10 :
                raise ValueError("Please guess a number within the given range")