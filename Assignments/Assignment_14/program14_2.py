
#################################################################################
#
#   Function Name : CubeNumber
#   Description   : Cube of number
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

CubeNumber = lambda No1 : No1*No1*No1


#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

def main():

    value = 0
    Ret = 0
    print("Enter a Number:-")
    value = int(input())

    Ret = CubeNumber(value)
    print("Cube of number is :", Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 3             Ouput : 27
#   Input1: 6             Ouput : 216
#7
#################################################################################