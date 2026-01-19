
#################################################################################
#
#   Function Name : CountDigit
#   Description   : Count number of Digit in a number
#   Input         : A Number
#   Output        : return Digit count
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def CountDigit(No1):

    Digit = 0
    Count = 0
    while(No1 != 0):
        Digit = No1 % 10
        No1 = No1 // 10
        Count = Count+1
    return Count

    

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
    
    Ret = CountDigit(iValue1)

    print("Digits are:", Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 12324         Ouput : 5
#   Input1: 143435        Ouput : 6 
#7
#################################################################################