
from functools import reduce

# function for filter (Filter elements which are greater than equal to 70 and less than equal to 90)
FilterX = lambda No1: No1 >= 70 and No1 <= 90     

# function increase each number by 10
MapX = lambda No1 : No1 + 10

# function return the product of all that elements
ReduceX = lambda No1 , No2 : No1*No2

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

    fdata = list(filter(FilterX , data))
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
#   Original List :- [4,34,36,76,68,24,89,23,86,90,45,70]
#   List after Filter :-[76,89,86,90,70]
#   List after Map :- [86,99,96,100,80]
#   Output after reduce:- 6538752000 
#
#################################################################################