
#################################################################################
#
#   Function Name : SumDigits
#   Description   : Sum Digits of number
#   Input         : A Number
#   Output        : summation
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def SumDigits(No1):

    Sum = 0
    digit = 0
    while(No1 != 0):
        digit = No1%10
        No1 = No1//10
        Sum = Sum +digit

    return Sum

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

    Ret = SumDigits(Value)

    print("Summation of digits :-", Ret)


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 12345                  Output: Summation of digits :-15
#                                           
#
#################################################################################