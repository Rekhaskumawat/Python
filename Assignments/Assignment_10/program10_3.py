
#################################################################################
#
#   Function Name : Factorial
#   Description   : Factorial of Number
#   Input         : A Number
#   Output        : Factorial
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def Factorial(No1):
    Fact = 1
    for i in range(1 ,No1+1):
        Fact = Fact*i
    return Fact

#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def main():

    iValue1 = 0
    Ret = 0
    print("Enter number:-")
    iValue1 = int(input())
    
    Ret = Factorial(iValue1)

    print("Factorial of a number:- ",Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 5        Ouput : 120
#   Input1: 6        Ouput : 720
#7
#################################################################################