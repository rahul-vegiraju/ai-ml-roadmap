import sys

if len(sys.argv) != 2:
    sys.exit(1)

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit(1)

try:
    with open(filename) as file:
        count = 0

        for line in file:
            stripped = line.strip()

            if stripped == "":
                continue

            if stripped.startswith("#"):
                continue

            count += 1

        print(count)

except FileNotFoundError:
    sys.exit(1)