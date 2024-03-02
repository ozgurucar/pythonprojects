# Step 1
import random

hangman_art = r'''
 __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. 
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| 
'''

stages = [r'''  
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

is_game_end = False
life_count = 6
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()
print(hangman_art)
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
display = []
chosen_word = random.choice(word_list)
guess_list = []
for letter in chosen_word:
    display += '_'

print(f"{' '.join(display)}")

while not is_game_end:
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    while guess in guess_list:
        guess = input("You've already made this guess, try another one: ").lower()
    guess_list.append(guess)
    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    index = 0
    for letter in chosen_word:
        if letter == guess:
            display[index] = guess
        index += 1
    if (guess not in chosen_word):
        life_count -= 1
        print(stages[life_count])
        if life_count == 0:
            print("Game Over")
            exit()

    if "_" not in display:
        print("You Win!")
        is_game_end = True
    print(f"{' '.join(display)}")
