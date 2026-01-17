
# factorial of a number


def Factorial(No):

    fact = 1

    for i in range(1,No+1):
        fact = fact*i

    return fact

def main():
    
    value = 0
    Ret = 0
    print("Enter a Number:-")
    value = int(input())
    Ret = Factorial(value)

    print("Factorial is :",Ret)

if __name__ == "__main__":
    main()