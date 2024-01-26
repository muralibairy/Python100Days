'''
Instructions
This is a difficult challenge. 💪

You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
Now it looks a bit more like the coordinates of a real map:

Map Coordinates Example

Your job is to write a program that allows you to mark a square on the map using a letter-number system.

List coordinates

So an input of A3 should place an X at the position shown below:

Exmaple location

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
Example Input 2
B1
Example Output 2
Hiding your treasure! X marks the spot.
['⬜️', 'X', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️️', '⬜️️']
Hints
See if this List method helps you: https://www.w3schools.com/python/ref_list_index.asp

Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

list = [['A', 'B, 'C'], 'E', 'F', 'G']
E is list[1] C is list[0][2]

Check your formatting. This is correctly formatted:
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
vs.

Incorrectly formatted (missing a space before 'X and extra space after the X and extra space before the comma):

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️','X ' , '⬜️']

'''


'''

Basic version of code

'''

'''
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

if position == 'A1':
  line1[0] = 'X'
elif position == 'A2':
  line2[0] = 'X'
elif position == 'A3':
  line3[0] = 'X'
elif position == 'B1':
  line1[1] = 'X'
elif position == 'B2':
  line2[1] = 'X'
elif position == 'B3':
  line3[1] = 'X'
elif position == 'C1':
  line1[2] = 'X'
elif position == 'C2':
  line2[2] = 'X'
elif position == 'C3':
  line3[2] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
'''


'''
2nd version of code
'''

'''
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

if position[0] == 'A':
    if position[1] == '1':
        line1[0] = 'X'
    if position[1] == '2':
        line2[0] = 'X'
    if position[1] == '3':
        line3[0] = 'X'
elif position[0] == 'B':
    if position[1] == '1':
        line1[1] = 'X'
    if position[1] == '2':
        line2[1] = 'X'
    if position[1] == '3':
        line3[1] = 'X'
elif position[0] == 'C':
    if position[1] == '1':
        line1[2] = 'X'
    if position[1] == '2':
        line2[2] = 'X'
    if position[1] == '3':
        line3[2] = 'X'
         
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
'''

''' Code version 3'''

'''
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

if position[0] == 'A':
    if position[1] == '1':
        map[map.index(line1)][0] = 'X'
    if position[1] == '2':
        map[map.index(line2)][0] = 'X'
    if position[1] == '3':
        map[map.index(line3)][0] = 'X'
elif position[0] == 'B':
    if position[1] == '1':
        map[map.index(line1)][1] = 'X'
    if position[1] == '2':
        map[map.index(line2)][1] = 'X'
    if position[1] == '3':
        map[map.index(line3)][1] = 'X'
elif position[0] == 'C':
    if position[1] == '1':
        map[map.index(line1)][2] = 'X'
    if position[1] == '2':
        map[map.index(line2)][2] = 'X'
    if position[1] == '3':
        map[map.index(line3)][2] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
'''

line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower()
abc = ["a", "b", "c"]

letter_index = abc.index(letter)
number_index = int(position[1]) - 1

map[number_index][letter_index] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

