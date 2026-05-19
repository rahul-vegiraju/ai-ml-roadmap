import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)

    if not match:
        return False
# We seperate into a list of 4 numbers
    numbers = match.groups()
#IPv4 numbers must be from 0 to 255. So it would be the first number in the list.
    for number in numbers:
        if int(number) < 0 or int(number) > 255:
            return False

    return True
if __name__ == "__main__":  
    main()