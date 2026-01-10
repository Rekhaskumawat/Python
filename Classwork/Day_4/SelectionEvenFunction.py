
# procedural approach
# check even, odd

def CheckEven(No):

    if(No % 2 == 0):
        print("Number is Even")
    else:
        print("Number is Odd")

def main():

    CheckEven(21)                           # positional argument
    CheckEven(No=22)                        # Keyword argument

if __name__ == "__main__":
    main()