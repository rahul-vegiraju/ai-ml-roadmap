def main():
    grocery = {}
    while True:
        try:
            user_input = input("Enter the item:").upper()
            if user_input in grocery:
                grocery[user_input] +=1
            else:
                grocery[user_input] = 1

        except EOFError:
            print()

            for item in sorted(grocery):
                print(grocery[item], item)
            break
main()