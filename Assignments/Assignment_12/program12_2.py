
#################################################################################
#
#   Function Name : Factor
#   Description   : factor of a number
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 20 / 01 / 2026
#
#################################################################################

def Factor(No1):

    for i in range(1 , No1+1):
        if(No1 % i == 0):
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

    Factor(value)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 12             Ouput : 1 2 3 4 6 12
#   Input1: 6              Ouput : 1 2 3 6 
#7
#################################################################################