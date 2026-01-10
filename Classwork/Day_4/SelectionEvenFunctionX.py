
# procedural approach ( input from user)
# check even, odd

def CheckEven(No):

    if(No % 2 == 0):
        print("Number is Even")
    else:
        print("Number is Odd")

def main():

    Value = 0
    print("Enter a Number:-")
    Value = int(input())
    CheckEven(Value)                                               

if __name__ == "__main__":
    main()