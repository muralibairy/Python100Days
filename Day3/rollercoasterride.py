def rollercoasterride(height, age):
    bill = 0
    if height > 120:
        if age < 12:
            bill += 5
        elif age == 12 or age <= 18:
            bill += 7
        elif age > 18:
            bill += 12
        want_photo = input("Do you want a photo? ")
        print(f"bill: {bill}")
        if want_photo == 'yes':
            bill += 3
            print(f"bill with photo: {bill}")
            return bill
        else:
            return bill
            print(f"bill without photo: {bill}")
    else:
        print("You do not meet the height criteria of 120 cm")
        return 0


height = int(input("Enter height in cm: "))
age = int(input("Enter age: "))

total_bill = rollercoasterride(height, age)
print(f"Your final bill is: {total_bill}")