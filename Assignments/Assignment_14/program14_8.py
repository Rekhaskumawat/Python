
#################################################################################
#
#   Function Name : Addition
#   Description   : Addition of two numbers
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

Addition = lambda No1,No2 : No1 +No2


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
    Ret = 0
    print("Enter first Number:-")
    value1 = int(input())

    print("Enter second Number:-")
    value2 = int(input())

    Ret = Addition(value1, value2)

    print("Addition is :", Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 50              Input2 :50              Output : 100
#   Input1: 6               Input2: 24              Output : 30
#7
#################################################################################