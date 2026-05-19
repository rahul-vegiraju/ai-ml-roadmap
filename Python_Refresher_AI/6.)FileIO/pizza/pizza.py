import sys
import csv

from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit(1)

csv_file_name = sys.argv[1]

if csv_file_name[-4:] != ".csv":
    sys.exit(1)

try:
    with open(csv_file_name) as file:
        reader = csv.reader(file)
        rows = list(reader)
        print(tabulate(rows[1:], headers=rows[0], tablefmt="grid"))


except FileNotFoundError:
    sys.exit(1)