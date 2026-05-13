user_input = input("Enter the string:")

def removeVowels(user_input):
    vowels = ["a","e","i","o","u"]
    res = []
    for ele in user_input.lower():
        if ele in vowels:
            continue
        else:
            res.append(ele)
    return "".join(res)

print(removeVowels(user_input))