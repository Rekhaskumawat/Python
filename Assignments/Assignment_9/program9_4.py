
#################################################################################
#
#   Function Name : cubeX
#   Description   : cube of number
#   Input         : A Number
#   Output        : return cube of number
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 17 / 01 / 2026
#
#################################################################################

def cubeX(No1):

    return No1*No1*No1


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
    iRet = 0

    print("Enter number:-")
    iValue1 = int(input())
    
    iRet = cubeX(iValue1)

    print("cube of number is:-", iRet)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 12        Ouput : 1728
#   Input1:  6        Ouput : 216
#
#################################################################################