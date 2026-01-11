
# List  Input from user

def main():

    Size = 0
    Value = 0 

    print("Enter the number of Element")

    Size = int(input())
    Data = list()

    print("Enter the Elements :")

    for i in range(Size):
        Value=  int(input())
        Data.append(Value)

    print(Data)

if __name__ == "__main__":
    main()