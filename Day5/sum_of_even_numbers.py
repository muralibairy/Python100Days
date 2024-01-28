"""all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

Example Input 1
10
Example Output 1
30
Example Input 2
52
Example Output 2
702
Hint
There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.

"""
# Enter a number between 0 and 1000

# 🚨 Do not change the code above ☝️

# Write your code here 👇
# even_sum = 0
# for n in range(0, target + 1, 2):
#   even_sum += n
# print(even_sum)
target = int(input("Enter target number: "))
print(target)
even_sum = 0
for n in range(0, target + 1):
    if n % 2 == 0:
        even_sum += n
print(even_sum)
