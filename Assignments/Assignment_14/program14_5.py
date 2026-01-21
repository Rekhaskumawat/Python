
#################################################################################
#
#   Function Name : Even
#   Description   : Even number
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

Even= lambda No1 :No1 % 2 == 0


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

    Ret = Even(value1 )

    print(Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 3                      Output : False
#   Input1: 6                      Output : True
#7
#################################################################################