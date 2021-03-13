"""A number-guessing game."""

#greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect
#         give hint
#         increase number of guesses
#     else:
#         congratulate player

import random 

player = input("Howdy, what's your name?")

print(f'{player}, I\'m thinking of a number between 1 and 100')

num = random.randint(1,100)
count = 0
condition = True
while condition:
    guess = int(input("Guess the number: "))
    if guess > num:
        print("Your guess was too big! Please try again")
        count = count + 1
    elif guess < num:
        print("Your guess was too low! Please try again")    
        count = count + 1
    else:
        condition = False
        
print(f"Congratulations {player}. You guessed the number correctly")
print(f"Number of guesses: {count}")
