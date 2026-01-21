
#################################################################################
#
#   Function Name : LargerNumber
#   Description   : largest number from three number
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

LargestNumber = lambda No1,No2, No3: max(No1 ,No2 ,No3)


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

    value1= 0
    value2 = 0
    value3 = 0
    Ret = 0
    print("Enter first Number:-")
    value1 = int(input())

    print("Enter second Number:-")
    value2 = int(input())

    print("Enter third Number:-")
    value3 = int(input())


    Ret = LargestNumber(value1, value2, value3)

    print("LargestNumber is :", Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 50              Input2 :50              Output : 2500
#   Input1: 6               Input2: 24              Output : 144
#7
#################################################################################