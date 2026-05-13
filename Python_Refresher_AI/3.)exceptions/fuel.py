def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")

            x,y = int(x), int(y)

            if y == 0 or x>y:
                continue

            percent = round((x/y)*100)

            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f'{percent}%')
            
            break

        except ValueError:
            continue
        except ZeroDivisionError:
            continue
main()


# user_input = input("Enter the fuel %:")

# def fuel(user_input):
#     X,Y = user_input.split("/")
#     res = (int(X)/int(Y))*100 
    
#     if res < 2:
#         print("E") 
#     elif res > 98:
#         print("F")
#     else:
#         print(str(round(res))+"%")

# fuel(user_input)