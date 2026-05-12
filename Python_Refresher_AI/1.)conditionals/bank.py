user_input = input("Enter the user greeting.").strip.lower()

if user_input[:5] == "hello":
    print("$0")
elif user_input[0] == "h":
    print("$20")
else:
    print("$100")


# greeting = input("Greeting: ").strip().lower()

# if greeting.startswith("hello"):
#     print("$0")
# elif greeting.startswith("h"):
#     print("$20")
# else:
#     print("$100")