def main():
    time = input("Enter a time: ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    minutes = int(time[-2:])
    decimal_value = minutes/60
    return (int(time[:-3])+decimal_value)


if __name__ == "__main__":
    main()