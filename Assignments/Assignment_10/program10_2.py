
#################################################################################
#
#   Function Name : Summation
#   Description   : Sum of first N natural number
#   Input         : A Number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 17 / 01 / 2026
#
#################################################################################

def Summation(No1):
    Sum = 0
    for i in range(1 ,No1+1):
        Sum = Sum+i
    return Sum

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
    
    Ret = Summation(iValue1)

    print("Sum of first N natural number is:- ",Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 5        Ouput : 15
#   Input1: 6        Ouput : 21
#
#################################################################################