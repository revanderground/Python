# Step 1

word_list = ["Venezia", "Toronto", "Shangai", "tree", "dragon", "punk"]

# TODO-1 - Randomly choose a word from the world_list and assign it to a variable called chosen_word.

import random

chosen_word = random.choice(word_list)

#TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess= input("Guess a letter:").lower()

#TODO-3 - Check if the letter the user guesssed (guess) is one of the letters in the chosen_word

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
