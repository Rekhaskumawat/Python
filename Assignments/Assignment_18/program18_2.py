
#################################################################################
#
#   Function Name : Maximum
#   Description   : maximum number from the list
#   Input         : A list
#   Output        : Maximum number
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def Maximum(Arr):

    Max = Arr[0]
    for i in range(len(Arr)):
        if(Max < Arr[i]):
            Max = Arr[i]

    return Max

#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def main():

    element = 0
    value = 0 
    print("Number of elements:-")
    element = int(input())

    Data = list()

    for i in range(element):

        value = int(input())
        Data.append(value)

    Ret = Maximum(Data)

    print("Maximum element from list is :-",Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 6        Input2 : 13 5 45 7 4 56    Output : 56
#
#################################################################################