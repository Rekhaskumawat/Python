
#################################################################################
#
#   Function Name : ChkGreater
#   Description   : check the greater number
#   Input         : two number
#   Output        : return greater number
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 17 / 01 / 2026
#
#################################################################################

def ChkGreater(No1 , No2):

    if(No1 > No2):
        return No1
    else:
        return No2


#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 17 / 01 / 2026
#
#################################################################################

def main():

    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter first number:-")
    iValue1 = int(input())
    print("Enter Second number:-")
    iValue2 = int(input())
    
    iRet = ChkGreater(iValue1, iValue2)

    print("Greater number is:-", iRet)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 12    Input2: 32    Ouput : 32
#   Input1: 56    Input2: 2     Ouput : 56
#
#################################################################################