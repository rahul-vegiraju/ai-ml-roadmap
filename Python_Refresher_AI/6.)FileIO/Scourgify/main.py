import csv
import sys

if len(sys.argv) != 3:
    sys.exit(1)

before = sys.argv[1]
after = sys.argv[2]

try:
    with open(before) as file:
        reader = csv.DictReader(file)

        students = []

        for row in reader:
            last, first = row["name"].split(", ")
            house = row["house"]

            students.append({
                "first": first,
                "last": last,
                "house": house
            })

except FileNotFoundError:
    sys.exit(1)

with open(after, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()

    for student in students:
        writer.writerow(student)