x = input("Enter the string")
def playback(x):
    res = []
    for ele in x: 
        if ele == " ":
            res.append("...")
        else:
            res.append(ele)
    end_res = "".join(res)
    print(end_res)

playback(x)