
#   implimentation of filter map reduce

from functools import reduce

#################################################################################
#
#   Function Name : Maximum
#   Description   : Maximum number
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

Maximum= lambda No1 , No2 : No1 if(No1>No2) else No2


#################################################################################
#
#   Function Name : main()
#   Description   : call another function and reduce the list
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

    rRet = reduce(Maximum , Data)

    print(rRet)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 1 2 3 4 5              Output : 5
#
#################################################################################