
#   implimentation of filter map reduce

#################################################################################
#
#   Function Name : odd
#   Description   : odd number
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

odd= lambda No1 :No1 % 2 == 1


#################################################################################
#
#   Function Name : main()
#   Description   : call another function and filter the list
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

def main():

    size = 0
    Ret = 0
    value = 0
    print("Enter a Number of elements:-")
    size = int(input())
    Data = list()
    print("Enter elements")

    for i in range(size):
        value = int(input())
        Data.append(value)

    fRet = list(filter(odd , Data))

    print(fRet)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 1 2 3 4 5              Output : [1,3,5]
#
#################################################################################