user_input = input("Enter the arithmetic expression:").strip()

x = int(user_input[0])
y = user_input[1]
z = int(user_input[2])

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print(result)