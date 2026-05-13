def main():
    word = input("Input:")
    print(shorten(word))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    res = []
    for ele in word:
        if ele.lower() in vowels:
            continue
        else:
            res.append(ele)

    return "".join(res)


if __name__ == "__main__":
    main()