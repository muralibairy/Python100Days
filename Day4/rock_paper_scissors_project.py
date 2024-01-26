"""
## Rock Paper Scissors

# Instructions

Make a rock, paper, scissors game.

Inside the `main.py` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`. This will make it easy to print them out to the console.

Start the game by asking the player:

*"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

From there you will need to figure out:
* How you will store the user's input.
* How you will generate a random choice for the computer.
* How you will compare the user's and the computer's choice to determine the winner (or a draw).
* And also how you will give feedback to the player.

You can find the "official" rules of the game on [the World Rock Paper Scissors Association website.](https://wrpsa.com/the-official-rules-of-rock-paper-scissors/)


# Solution

[https://replit.com/@appbrewery/rock-paper-scissors-end](https://replit.com/@appbrewery/rock-paper-scissors-end)

"""

""" Initial Version of code """

"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("Enter a number:\n0 for Scissors\n1 for Rock\n2 for Paper\n"))

gesture = [scissors, rock, paper]
length = len(gesture)

computer_choice = random.randint(0, length-1)

print(f"Computer choose: {gesture[computer_choice]}")

if choice == 0:
    print(f"You choose: {scissors}")
elif choice == 1:
    print(f"You choose: {rock}")
else:
    print(f"You choose: {paper}")

print(f"Computer's choice: {computer_choice} \nYour choice: {choice}")

'''3 Rules:
Rock wins against scissors
Scissors wins against paper
Paper wins against rock'''

# Rock > scissors
# scissors > paper
# paper > rock

'''scissors = 0, rock = 1, paper = 2'''
win = False

if computer_choice == 0 and choice == 0 or computer_choice == 1 and choice == 1 or computer_choice == 2 and choice == 2:
    print("Game Draw!")
elif computer_choice == 1 and choice == 0:
    print("Computer win!")
elif choice == 1 and computer_choice == 0:
    print("You win!")
elif choice == 0 and computer_choice == 2:
    print("You win!")
elif choice == 2 and computer_choice == 1:
    print("You win!")
elif choice == 1 and computer_choice == 2:
    print("Computer win!")
else:
    print("Computer win!")

"""


"""  A final version of code """

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you type? Enter\n0 for Rock \n1 for Paper\n2 for Scissors\n"))
if user_choice >= 3 and user_choice < 0:
    print("You typed an invalid number, you loose")
else:
    computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")

if computer_choice > user_choice:
    print("You Lose!")
