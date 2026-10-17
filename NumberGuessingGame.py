print("=======Number Guessing Game=======")
print("Guess the number between 1 to 10")
guess = int(input("enter your guess: "))
if guess <= 5:
    print("COLD!!!")
    print("Try again")
elif guess >= 5 or guess <= 10 :
    print("WARM!!!")
    print("Good try")
    print("Try again")
else: 
    guess = 10
    print("Correct answer!!!")
    print("You win!!!")
guess = "Guessed more than 5 times "
if guess:
    print("You have lost")
else: 
    print("You have won")