
#################################################################################
#
#   Function Name : ReverseDigit
#   Description   : reverse the original digit
#   Input         : A Number
#   Output        : Reversed digit
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def ReverseDigit(No1):

    Digit = 0
    Rev = 0
    while(No1 != 0):
        Digit = No1 % 10
        No1 = No1 // 10
        Rev = Rev*10 + Digit

    return Rev

    

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
    
    Ret = ReverseDigit(iValue1)

    print("Reverse of Digit:",Ret)


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 12324         Ouput : 42321
#   Input1: 143435        Ouput : 534341 
#7
#################################################################################