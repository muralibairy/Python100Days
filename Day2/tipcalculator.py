'''
Welcome to the tip calculator.
What was the total bill? 124.56
What percentage tip would you like to give? 10, 12, or 15? 12
How may people to split the bill? 7
Each person should pay: $19.93
150 = 12 percent is 12/100 = 0.12 => 150 * 0.12 = 18.0 => 150 + 18 = 168 =>
150 * 1.12 = 168.0000000
168/5 = 33.6
then it should show the tip
'''

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How may people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(final_amount)
