from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    birthdate = input("Date of Birth: ")
    try:
        birthday = parse_date(birthdate)
    except ValueError:
        sys.exit("Invalid date")

    minutes = calculate_minutes(birthday)
    print(convert_to_words(minutes))


def parse_date(s):
    return date.fromisoformat(s)


def calculate_minutes(birthday):
    today = date.today()
    days = (today - birthday).days
    return days * 24 * 60


def convert_to_words(minutes):
    words = p.number_to_words(minutes, andword="")
    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()