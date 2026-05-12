#The way I did at first was too complicated but works.
#res = input[:4:-1]
#res[::-1]


file = input("File name: ").strip().lower()

if file[-4:] == ".gif":
    print("image/gif")
elif file[-4:] == ".jpg" or file[-5:] == ".jpeg":
    print("image/jpeg")
elif file[-4:] == ".png":
    print("image/png")
elif file[-4:] == ".pdf":
    print("application/pdf")
elif file[-4:] == ".txt":
    print("text/plain")
elif file[-4:] == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")

# file = input("File name: ").strip().lower()

# if file.endswith(".gif"):
#     print("image/gif")
# elif file.endswith(".jpg") or file.endswith(".jpeg"):
#     print("image/jpeg")
# elif file.endswith(".png"):
#     print("image/png")
# elif file.endswith(".pdf"):
#     print("application/pdf")
# elif file.endswith(".txt"):
#     print("text/plain")
# elif file.endswith(".zip"):
#     print("application/zip")
# else:
#     print("application/octet-stream")