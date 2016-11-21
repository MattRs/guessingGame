""" Guess a number between 1 - 10 """

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print(random_number)

guesses_left = 3
# Start your game!


while guesses_left >=1:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print("You win!")
        break
    guesses_left -= 1
else:
    print("You lose.")