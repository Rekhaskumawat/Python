
from functools import reduce

#################################################################################
#
#   Function Name : ChkPrime
#   Description   : list of prime numbers
#   Input         : List
#   Output        : List
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 25 / 01 / 2026
#
#################################################################################

def ChkPrime(Arr):

    if Arr <= 3 and Arr > 0:
        return Arr
    bFlage = True
    for j in range(2 , Arr//2):
        if(Arr % j == 0):
            bFlage = False
            break
    
    if(bFlage == True):
        return Arr 

# function multiply each number by 2
MapX = lambda No1 : No1*2

# function return the Sum of all that elements
ReduceX = lambda No1 , No2 : No1 if (No1 >No2) else  No2

#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 25 / 01 / 2026
#
#################################################################################

def main():

    Size = 0
    value =0
    data = list()

    print("Number of elements:-")
    size = int(input())

    print("Enter the elements:-")

    for i in range(size):
        value = int(input())
        data.append(value)
    print("original List :-", data)
    
    fdata = list(filter(ChkPrime, data))
    print("List after filter :-", fdata)

    mdata = list(map(MapX , fdata))
    print("List after map :-",mdata)

    rdata = reduce(ReduceX ,mdata)
    print("Output after reduce:-",rdata)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Original List :- [2,70,11,10,17,23,31,77]
#   List after Filter :-[2,11,17,23,31]
#   List after Map :- [4,22,34,46,62]
#   Output after reduce:- 62
#
#################################################################################