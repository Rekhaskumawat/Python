
#################################################################################
#
#   Function Name : ReverseNumber
#   Description   : Print number in reverse order
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 20 / 01 / 2026
#
#################################################################################

def ReverseNumber(No1):

    for i in range(No1 , 0 ,-1):
        print(i)


#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 20 / 01 / 2026
#
#################################################################################

def main():

    value = 0
    print("Enter a Number:-")
    value = int(input())

    ReverseNumber(value)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 3             Ouput : 3 2 1
#   Input1: 6             Ouput : 6 5 4 3 2 1
#7
#################################################################################