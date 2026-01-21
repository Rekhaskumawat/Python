
#################################################################################
#
#   Function Name : Minimum
#   Description   : Minimum number
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

Minimum = lambda No1 ,No2: No1 if (No1<No2) else No2


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
    value2 =0
    Ret = 0
    print("Enter first Number:-")
    value1 = int(input())

    print("Enter second Number:-")
    value2 = int(input())

    Ret = Minimum(value1 , value2)
    print("Minimum number :", Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 3             Input2: 21           Output : Minimum number :- 3
#   Input1: 6             Input2 : 34          Output : Minimum number :-6
#7
#################################################################################