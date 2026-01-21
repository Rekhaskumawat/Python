
#   implimentation of filter map reduce


#################################################################################
#
#   Function Name : DivisibleBy5and3
#   Description   : Number Divivsible By 5 and 3
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

DivisibleBy5and3= lambda No1 : No1 % 5 == 0 and No1 % 3 == 0


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

    rRet = list(filter(DivisibleBy5and3 , Data))

    print(rRet)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 10 30 15 40 60            Output : [30 , 15 , 60]
#
#################################################################################