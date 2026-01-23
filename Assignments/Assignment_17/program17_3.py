
#################################################################################
#
#   Function Name : Factorial
#   Description   : return factorial of a number
#   Input         : A Number
#   Output        : factorial
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def Factorial(No1):
    
    fact = 1
    for i in range(1 ,No1+1):
        fact = fact*i
    return fact  

#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def main():

    Value = 0
    Ret = 0
    print("Enter the Number :-")
    Value = int(input())

    Ret = Factorial(Value)
    print("Factorial is :-", Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 5                       Output: 120
#    Input : 3                       Output : 6
#
#################################################################################