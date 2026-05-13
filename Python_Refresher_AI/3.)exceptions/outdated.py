
#need to do again. Wasnt able to do.

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        else:
            month_day, year = date.split(",")

            month_name, day = month_day.split()

            month = months.index(month_name) + 1
            day = int(day)
            year = int(year.strip())

        if month > 12 or day > 31:
            continue

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except ValueError:
        continue