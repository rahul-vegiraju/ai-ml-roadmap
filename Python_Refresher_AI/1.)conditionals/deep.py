user_input = input("What is the answer to the Great Question of Life, the Universe and Everything")
def deep(user_input):
    if user_input == "42":
        print("yes")
    elif user_input == "forty two":
        print("yes")
    elif user_input == "forty-two":
        print("yes")
    else:
        print("no")
    
deep(user_input)



# answer = input("Answer: ").strip().lower()

# if answer == "42" or answer == "forty-two" or answer == "forty two":
#     print("Yes")
# else:
#     print("No")