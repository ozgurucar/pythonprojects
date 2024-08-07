import random

"""test commit"""
game_level = input("Select level by writing 'easy' or 'hard' \n")

lives = 0
if game_level.lower() == "easy":
    lives = 10
elif game_level.lower() == "hard":
    lives = 5

number = random.randint(0, 100)
selection = -1

while selection != number and lives > 0:
    selection = int(input(f"You have {lives} chance to guess, Guess the number between [0, 100] \n"))

    if selection > number:
        print("Too High")

    elif selection < number:
        print("Too Low")

    lives -= 1

if selection == number:
    print(f"You won!, the number was {number}")
elif lives <= 0:
    print("You Lost!")
