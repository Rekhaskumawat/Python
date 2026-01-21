
#################################################################################
#
#   Function Name : PerfectNumber
#   Description   : checks the perfect number
#   Input         : A number
#   Output        : return the perfect number
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def PerfectNumber(No1):
    sum = 0
    for i in range(1 , No1):
        if(No1 % i == 0):
            sum = sum + i
    return sum


#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def main():

    value = 0
    print("Enter a Number:-")
    value = int(input())

    Ret = PerfectNumber(value)

    if Ret == value:
        print("Number is perfect number")
    else:
        print("number is not a perfect number")


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 3             Ouput : Number is not a perfect number
#   Input1: 6             Ouput : number is a perfect number
#7
#################################################################################