"""
Hangman project, example game in below url
https://hangmanwordgame.com/?fca=1&success=0#/
"""

import random

word_list = ["Anirudh", "Agastya", "Parijatha", "Muralidhar"]

chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
# print(f"word length: {word_length}")
display = []
for _ in range(word_length):
    display += "_"

# print(f"chosen_word: {chosen_word}")

print(f"display: {display}")


'''
i = 0
for letter in chosen_word:
    if letter == guess:
        display[i] = letter
    i += 1
'''
position = 0
flag = 0
while flag < word_length:
    guess = input("Guess a letter: ").lower()
    if guess.isalpha():
        if len(guess) == 1:
            for i in range(word_length):
                letter = chosen_word[i]
                if letter == guess:
                    display[i] = guess
                    flag += 1
            print(f"display: {display}")
            if flag == word_length:
                print("You win!")
        else:
            print("Enter a single character")
    else:
        print("Enter an alphabet")