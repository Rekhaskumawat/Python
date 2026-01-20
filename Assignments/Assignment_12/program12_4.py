
#################################################################################
#
#   Function Name : PrintNumber
#   Description   : Print number till that number
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 20 / 01 / 2026
#
#################################################################################

def PrintNumber(No1):

    for i in range(1 , No1+1):
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

    PrintNumber(value)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 3             Ouput : 1 2 3
#   Input1: 6             Ouput : 1 2 3 4 5 6
#7
#################################################################################