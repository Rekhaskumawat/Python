
#   implimentation of filter map reduce


#################################################################################
#
#   Function Name : length5
#   Description   : length of string is greater than 5
#   Input         : A string
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

length5= lambda name : len(name) > 5 


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

    Ret = 0
    name = 0
    elements = 0
    Data = list()

    print("Enter the number of names:-")
    elements = int(input())

    print("Enter elements")

    for i in range(elements):
        name = input()
        Data.append(name)

    rRet = list(filter(length5 , Data))

    print(rRet)

# starter
if __name__ == "__main__":
    main()

#######################################################################################################
#
#   Input1: rekha , shubham , riddhi ,siddhi ,kumawat    output:[shubham , riddhi , siddhi , kumawat]
#
########################################################################################################