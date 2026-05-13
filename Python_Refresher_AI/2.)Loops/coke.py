amt_due = 50

while amt_due > 0:
    print("Amt Due:", amt_due)
    user_input = int(input("Enter the cents:"))

    if user_input == 25 or user_input == 10 or user_input == 5:
        amt_due -= user_input

change = amt_due *-1
print("Change", change)
