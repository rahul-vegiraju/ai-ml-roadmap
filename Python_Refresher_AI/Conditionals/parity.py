
class Solution(): 
    def main():
        x = int(input("enter number"))
        Solution.is_even(x)

    def is_even(x):
        if x % 2 == 0:
            print("Even")
        else:
            print("Odd")

Solution.main()  