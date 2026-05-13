user_input = input("Enter the name:")
myList = []
for ele in user_input:
    if ele.isupper():
        myList.append("_"+ele.lower())
    else:
        myList.append(ele)

print("".join(myList))