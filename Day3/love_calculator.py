""" Basic level of code - beginner"""
import random

"""
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

concatenated_names = name1 + name2
count_t = 0
names_lower = concatenated_names.lower()
for i in names_lower:
  if i == 't':
    count_t += 1
#print(f"T occures {count_t} times")

count_r = 0
for i in names_lower:
  if i == 'r':
    count_r += 1
#print(f"R occures {count_r} times")

count_u = 0
for i in names_lower:
  if i == 'u':
    count_u += 1
#print(f"U occures {count_u} times")

count_e = 0
for i in names_lower:
  if i == 'e':
    count_e += 1
#print(f"E occures {count_e} times")

total_in_true = count_t + count_r + count_u + count_e

#print(f"Total = {total_in_true}")

count_l = 0
for i in names_lower:
  if i == 'l':
    count_l += 1
#print(f"L occures {count_l} times")

count_o = 0
for i in names_lower:
  if i == 'o':
    count_o += 1
#print(f"O occures {count_o} times")

count_v = 0
for i in names_lower:
  if i == 'v':
    count_v += 1
#print(f"V occures {count_v} times")

count_e_love = 0
for i in names_lower:
  if i == 'e':
    count_e_love += 1
#print(f"E occures {count_e_love} times")

total_in_love = count_l + count_o + count_v + count_e_love

#print(f"Total = {total_in_love}")
love_score = str(total_in_true) + str(total_in_love)

#print(f"Your score is {love_score}")
int_love_score = int(love_score)
if int_love_score <= 10 or int_love_score >= 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int_love_score >= 40 and int_love_score <= 50:
  print(f"Your score is {int_love_score}, you are alright together.")
else:
  print(f"Your score is {int_love_score}.")
"""

""" Advanced level of code"""

print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# T = (name1 + name2).lower().count('t')
# R = (name1 + name2).lower().count('r')
# U = (name1 + name2).lower().count('u')
# E = (name1 + name2).lower().count('e')
#
# L = (name1 + name2).lower().count('l')
# O = (name1 + name2).lower().count('o')
# V = (name1 + name2).lower().count('v')
# E = (name1 + name2).lower().count('e')
#
# love_score = str(T + R + U + E) + str(L + O + V + E)
# love_score = int(love_score)
# if love_score <= 10 or love_score >= 90:
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 and love_score <= 50:
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}.")

'''Using random'''
# love_score = random.randint(1, 100)
# if love_score <= 10 or love_score >= 90:
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 and love_score <= 50:
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}.")