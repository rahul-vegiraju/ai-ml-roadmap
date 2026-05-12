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