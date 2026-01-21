
#################################################################################
#
#   Function Name : Odd
#   Description   : Odd number
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

Odd = lambda No1 : No1 % 2 == 1


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
    Ret = 0
    print("Enter a Number:-")
    value1 = int(input())

    Ret = Odd(value1 )

    print(Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 3                     Output : True
#   Input1: 6                     Output : False
#7
#################################################################################