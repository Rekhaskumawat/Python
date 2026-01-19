
#################################################################################
#
#   Function Name : SumDigit
#   Description   : Sum of Digits of Number
#   Input         : A Number
#   Output        : return sum of Digits
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def SumDigit(No1):

    Digit = 0
    Sum = 0
    while(No1 != 0):
        Digit = No1 % 10
        No1 = No1 // 10
        Sum = Sum+Digit
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
    print("Enter number:-")
    iValue1 = int(input())
    
    Ret = SumDigit(iValue1)

    print("Sum of Digits is :", Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 12324         Ouput : 12
#   Input1: 143435        Ouput : 20 
#7
#################################################################################