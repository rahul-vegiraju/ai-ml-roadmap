import csv

total = 0
count = 0
highest_sale = 0
highest_person = ""

with open("Python_Refresher_AI/action_items/CSV/sales.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        amount = float(row["amount"])

        total += amount
        count += 1

        if amount > highest_sale:
            highest_sale = amount
            highest_person = name

average = total / count

with open("Python_Refresher_AI/action_items/CSV/report.txt", "w") as report:
    report.write("Sales Report\n")
    report.write("------------\n")
    report.write(f"Total Sales: ${total:.2f}\n")
    report.write(f"Average Sale: ${average:.2f}\n")
    report.write(f"Highest Sale: ${highest_sale:.2f}\n")
    report.write(f"Top Person: {highest_person}\n")

print("Report created successfully.")