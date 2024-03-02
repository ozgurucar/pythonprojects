# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
display = []
chosen_word = random.choice(word_list)

for letter in chosen_word:
    display += '_'
print(display)

print("Chosen Word: " + chosen_word)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
index = 0
for letter in chosen_word:
    if letter == guess:
        display[index] = guess
    index += 1
    print(index)

print(display)
