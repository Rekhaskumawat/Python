
from functools import reduce

# function for filter (Filter elements which are Even)
FilterX = lambda No1: No1 % 2 == 0    

# function which calculate its square
MapX = lambda No1 : No1*No1

# function return the Sum of all that elements
ReduceX = lambda No1 , No2 : No1+No2

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
#   Original List :- [5,2,3,4,3,4,1,2,8,10]
#   List after Filter :-[2,4,4,2,8,10]
#   List after Map :- [4,16,16,4,64,100]
#   Output after reduce:- 204
#
#################################################################################