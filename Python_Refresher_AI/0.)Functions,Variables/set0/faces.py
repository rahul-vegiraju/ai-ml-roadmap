def convert(text):
    res = []
    i = 0

    while i < len(text):
        if i + 1 < len(text) and text[i] == ":" and text[i + 1] == ")":
            res.append("🙂")
            i += 2
        elif i + 1 < len(text) and text[i] == ":" and text[i + 1] == "(":
            res.append("🙁")
            i += 2
        else:
            res.append(text[i])
            i += 1

    return "".join(res)

def main():
    x = input("Enter the string: ")
    print(convert(x))

main()



# def convert(text):
#     text = text.replace(":)", "🙂")
#     text = text.replace(":(", "🙁")
#     return text

# def main():
#     x = input("Enter the string: ")
#     print(convert(x))

# main()
