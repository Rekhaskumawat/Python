
#################################################################################
#
#   Function Name : Frequency
#   Description   : Frequency of a number from the list
#   Input         : A list , number
#   Output        : Frequency
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def Frequency(Arr , search):

    count = 0
    for i in range(len(Arr)):
        if(search ==  Arr[i]):
            count = count+1

    return count

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
    search = 0
    value = 0 

    print("Number of elements:-")
    element = int(input())

    print("Enter the number you want to search:-")
    search = int(input())

    Data = list()

    for i in range(element):

        value = int(input())
        Data.append(value)

    Ret = Frequency(Data , search)

    print("Frequency of element from list is :-",Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 6        Input2 : 13 5 45 7 4 56    Output : 56
#
#################################################################################